
var circle = function(r){
return function(v){
return [r*COS(v[0]),r*SIN(v[0])];
};
};
function CYLINDER(r,h){
var domain = DOMAIN([[-2*PI,2*PI]])([50]);
var crc = circle(r);
var model = MAP(crc)(domain);
return EXTRUDE([h])(model);
};

var random_generator = function(x,y,m){
	n = 1
	/*for the settlements*/
	if((x<=6 && x>=2 && y<=6 && y>=2)||(x<=15 && x>=11 && y<=6 && y>=2)||(x<=21 && x>=13 && y<=21 && y>=13))
		n = 0
var z = (COS(x)+SIN(y)*Math.random()*2)*COS(x/2) * n;
a = new Array();
a.push(x)
a.push(y)
a.push(z)
m.push(a)
return z; 
};

/* the matrix that contains the random values of z given x,y coordinates, useful fot the dtm model*/
var matrix = new Array();

/*dom dimensions*/
X_DOM = 10
Y_DOM = 20

/*lakes position*/
lake_dim = 5 
lake1_x = 3
lake1_y = 6
lake2_x = 29
lake2_y = 5
/*dtm dimensions*/
xvalue_dtm = 3.45
yvalue_dtm = 2
var domain = DOMAIN([[0, X_DOM], [0, Y_DOM]])([60,60]);


/****************************************************THE DTM MODEL ******************************************************/

var dtm_model = function (u1,v1) {
  return function (v) {
  	var a = v[0];
    var b = v[1];
   
    return [a*u1, b*v1 ,random_generator(a*u1,b*v1,matrix)];
  };
};

var mapping = dtm_model(xvalue_dtm,yvalue_dtm);
var model = MAP(mapping)(domain);
dtm = COLOR([205/255,133/255,63/255])(model)

/******************************************************THE LAKES**************************************************/

lake1 = COLOR([0,178/255,238/255,0.8])(CUBOID([lake_dim,lake_dim,1.4]))
lake2 = COLOR([0,178/255,238/255,0.8])(CUBOID([lake_dim,lake_dim,1.4]))

dtm_lake = STRUCT([dtm,T([2])([-2.2])(T([0])([lake1_x])(T([1])([lake1_y])(lake1))),T([2])([-1.5])(T([0])([lake2_x])(T([1])([lake2_y])(lake2)))])



/**************************************************THE TREES *****************************************************/

tree = function (h,r,d){
var domain = DOMAIN([[0,1],[0,2*PI]])([d,d]);
var profile1 = BEZIER(S0)([[0,0,0],[h,0,0]]);
var profile2 = BEZIER(S0)([[h,0,0],[0,0,2*h]]);

var mapping1 = ROTATIONAL_SURFACE(profile1);
var mapping2 = ROTATIONAL_SURFACE(profile2);
var surface1 = MAP(mapping1)(domain);
var surface2 = MAP(mapping2)(domain);

hairtree =  COLOR([0,100/255,0])(STRUCT([surface1,surface2]))
trunk = COLOR([133/255,94/255,66/255])(CYLINDER(r,h))
return STRUCT([trunk,T([2])([h])(hairtree)])

}

/*the trees can't be where are the lakes*/
checkPositionTree = function(x,y){
	if(!((x>=lake1_x && x<=lake1_x+lake_dim && y>=lake1_y && y<=lake1_y+lake_dim)||
		(x>=lake2_x && x<=lake2_x+lake_dim && y>=lake2_y && y<=lake2_y+lake_dim)))
		return true
	else 
		return false
}

/*generate a line of the a forest */
coniferous_forest_line = function(matrix_element,n){
t = tree(0.2,0.05,20)
x = matrix[matrix_element][0]
y = matrix[matrix_element][1]
z = matrix[matrix_element][2]
tree1 = T([2])([z])(T([1])([y])(T([0])([x])(t)))
forest = STRUCT([tree1])
for (var i = 0 ; i <= n; i++) {
	
	matrix_element = matrix_element +1
	x = matrix[matrix_element][0]
	y = matrix[matrix_element][1]
	z = matrix[matrix_element][2]

	if(checkPositionTree(x,y))
	forest = STRUCT([forest,T([2])([z])(T([1])([y])(T([0])([x])(t)))])
}
return forest
}

/*generate a forest*/
coniferous_forest = function(num_lines,num_trees,position){
n = 39

forest = coniferous_forest_line(position,num_trees)
thous = 0
if(position>=1000 && position<=1999){
	thous = 1
position = position-1000+1
}
if(position>=2000 && position<=2999){
	thous = 2
position = position-2000+1
}
for (var i = 2 ; i <= num_lines; i++) {
	
forest = STRUCT([forest,coniferous_forest_line((position*i)+(1000*thous)-n*(i-1),num_trees)])
}
return forest
}



forest1 = coniferous_forest(4,10,100)
forest2 = coniferous_forest(4,5,2000)


/*the model with dtm,forest and lakes*/
dtm_lake_forest = STRUCT([dtm_lake,forest1,forest2])



/********************************************************THE SETTLEMENT****************************************/
random_settlement_line = function(n){
xrand = Math.random()*0.5
yrand = Math.random()*0.5
zrand = Math.random()*0.5

settlements_line = CUBOID([xrand,yrand,zrand])
for (var i = 1; i <=n; i++) {
xrand = Math.random()*0.5
yrand = Math.random()*0.5
zrand = Math.random()*0.5
settlements_line = STRUCT([settlements_line,T([1])([0.5*i])(CUBOID([xrand,yrand,zrand]))])
};

return settlements_line
}

settlements = COLOR([1,1,1])(STRUCT([random_settlement_line(2),T([1])([2])(random_settlement_line(2)),
	T([1])([2])(T([0])([1])(random_settlement_line(2))),T([0])([1])(random_settlement_line(2))]))

settlements_traslated = STRUCT([T([1])([2.5])(T([0])([3])(settlements)),T([1])([2.5])(T([0])([13])(settlements))
	,T([1])([15])(T([0])([13.5])(settlements)),T([1])([15])(T([0])([16])(settlements)),T([1])([15])(T([0])([19])(settlements))])

/******************************************THE MODEL*************************************/
model_with_settlements = STRUCT([settlements_traslated,dtm_lake_forest])
