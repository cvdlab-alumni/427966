
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
var z = (COS(x)+SIN(y)*Math.random()*2)*COS(x/2);
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


/*THE DTM MODEL */

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


