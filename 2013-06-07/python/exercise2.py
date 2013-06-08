
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


#****************************************************THE DTM MODEL ****************************************************#

def dtm_model(v):
	a = v[0]
	b = v[1]
	return [a*xvalue_dtm, b*yvalue_dtm ,random_generator(a*xvalue_dtm,b*yvalue_dtm,matrix)]
   
model = MAP(dtm_model)(domain)
dtm = COLOR([0.8,0.521,0.247])(model)

#*******************************************************THE LAKES****************************************************************#

lake1 = COLOR([0,0.698,0.933,0.8])(CUBOID([lake_dim,lake_dim,1.4]))
lake2 = COLOR([0,0.698,0.933,0.8])(CUBOID([lake_dim,lake_dim,1.4]))


#**********************************THE MODEL*******************************************************#
dtm_lake = STRUCT([dtm,T([3])([-2.2])(T([1])([lake1_x])(T([2])([lake1_y])(lake1))),T([3])([-1.5])(T([1])([lake2_x])(T([1])([lake2_y])(lake2)))])


