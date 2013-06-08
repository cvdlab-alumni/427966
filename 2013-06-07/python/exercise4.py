
import random

def random_generator(x,y,m):
	z = (COS(x)+SIN(y)*random.random()*2)*COS(x/2);
	a = []
	a.append(x)
	a.append(y)
	a.append(z)
	m.append(a)
	return z; 


# the matrix that contains the random values of z given x,y coordinates, useful fot the dtm model#
matrix = []

#dom dimensions#
X_DOM = 10
Y_DOM = 20

#lakes position#
lake_dim = 5 
lake1_x = 3
lake1_y = 6
lake2_x = 29
lake2_y = 5
#dtm dimensions#
xvalue_dtm = 3.45
yvalue_dtm = 2
domain_x = INTERVALS(X_DOM)(60)
domain_y = INTERVALS(Y_DOM)(60)
domain = PROD([domain_x,domain_y])


#***************************************************THE DTM MODEL *****************************************************#

def dtm_model(v):
	a = v[0]
	b = v[1]
	return [a*xvalue_dtm, b*yvalue_dtm ,random_generator(a*xvalue_dtm,b*yvalue_dtm,matrix)]
   
model = MAP(dtm_model)(domain)
dtm = COLOR([0.8,0.521,0.247])(model)

#*****************************************************THE LAKES*************************************************#

lake1 = COLOR([0,0.698,0.933,0.8])(CUBOID([lake_dim,lake_dim,1.4]))
lake2 = COLOR([0,0.698,0.933,0.8])(CUBOID([lake_dim,lake_dim,1.4]))


dtm_lake = STRUCT([dtm,T([3])([-2.2])(T([0])([lake1_x])(T([2])([lake1_y])(lake1))),T([3])([-1.5])(T([1])([lake2_x])(T([2])([lake2_y])(lake2)))])





#*************************************************THE TREES ****************************************************#


def tree(h,r,d):
 	domain1 = INTERVALS(1)(d);
	domain2 = INTERVALS(2*PI)(d);
	domain = PROD([domain1,domain2])
	profile1 = BEZIER(S1)([[0,0,0],[h,0,0]]);
	profile2 = BEZIER(S1)([[h,0,0],[0,0,2*h]]);

	mapping1 = ROTATIONALSURFACE(profile1);
	mapping2 = ROTATIONALSURFACE(profile2);
	surface1 = MAP(mapping1)(domain);
	surface2 = MAP(mapping2)(domain);

	hairtree =  COLOR([0,0.392,0])(STRUCT([surface1,surface2]))
	trunk = COLOR([0.521,0.368,0.258])(CYLINDER([r,h])(30))
	return STRUCT([T([3])([h])(hairtree)])



#the trees can't be where are the lakes#
def checkPositionTree(x,y):
	if(not((x>=lake1_x and x<=lake1_x+lake_dim and y>=lake1_y and y<=lake1_y+lake_dim) or 
		(x>=lake2_x and x<=lake2_x+lake_dim and y>=lake2_y and y<=lake2_y+lake_dim))):
		return True
	else:
		return False


#generate a line of the a forest #
def coniferous_forest_line(matrix_element,n):
	
	t = tree(0.2,0.05,20)
	x = matrix[matrix_element][0]
	y = matrix[matrix_element][1]
	z = matrix[matrix_element][2]
	tree1 = T([3])([z])(T([2])([y])(T([1])([x])(t)))
	forest = STRUCT([tree1])
	for i in range(0,n): 
		matrix_element = matrix_element +1
		x = matrix[matrix_element][0]
		y = matrix[matrix_element][1]
		z = matrix[matrix_element][2]

		if(checkPositionTree(x,y)):
			forest = STRUCT([forest,T([3])([z])(T([2])([y])(T([1])([x])(t)))])

	return forest


#generate a forest#
def coniferous_forest(num_lines,num_trees,position):
	n = 39

	forest = coniferous_forest_line(position,num_trees)
	thous = 0
	if(position>=1000 and position<=1999):
		thous = 1
		position = position-1000+1

	if(position>=2000 and position<=2999):
		thous = 2
		position = position-2000+1

	for i in range(2,num_lines):
		forest = STRUCT([forest,coniferous_forest_line((position*i)+(1000*thous)-n*(i-1),num_trees)])

	return forest




forest1 = coniferous_forest(4,10,100)
forest2 = coniferous_forest(4,10,2000)


dtm_lake_forest = STRUCT([dtm_lake,forest1,forest2])

#*******************************************************THE SETTLEMENT***************************************#
def random_settlement_line(n):
	xrand = random.random()*0.5
	yrand = random.random()*0.5
	zrand = random.random()*0.5

	settlements_line = CUBOID([xrand,yrand,zrand])
	for i in range(1,n):
	xrand = random.random()*0.5
	yrand = random.random()*0.5
	zrand = random.random()*0.5
	settlements_line = STRUCT([settlements_line,T([2])([0.5*i])(CUBOID([xrand,yrand,zrand]))])


return settlements_line
}

settlements = COLOR([1,1,1])(STRUCT([random_settlement_line(2),T([2])([2])(random_settlement_line(2)),
	T([2])([2])(T([0])([1])(random_settlement_line(2))),T([1])([1])(random_settlement_line(2))]))

settlements_traslated = STRUCT([T([2])([2.5])(T([1])([3])(settlements)),T([2])([2.5])(T([0])([13])(settlements))
	,T([2])([15])(T([1])([13.5])(settlements)),T([2])([15])(T([1])([16])(settlements)),T([2])([15])(T([1])([19])(settlements))])

#*****************************************THE MODEL************************************#
model_with_settlements = STRUCT([settlements_traslated,dtm_lake_forest])
