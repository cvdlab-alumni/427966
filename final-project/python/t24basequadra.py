
def semicircle_a(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
	return semia

def semicircle_b(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
	return semib

domain1 = INTERVALS(1)(32);
domain2 =  PROD([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)

##############################################T24 BASE QUADRA TABLE############################################################

#THE CURVES OF THE UP PART OF THE TABLE#

curve1a_tableup = semicircle_a(2,1.3,0,0,0,0,0)
curve1b_tableup = semicircle_b(2,1.3,0,0,0,0,0)
curve2a_tableup = semicircle_a(2.05,1.35,0.03,0,0,0,0)
curve2b_tableup = semicircle_b(2.05,1.35,0.03,0,0,0,0) 
curve3a_tableup = semicircle_a(2,1.3,0.06,0,0,0,0)
curve3b_tableup = semicircle_b(2,1.3,0.06,0,0,0,0)

#THE MAPS OF THE UP PART OF THE TABLE#
map1_tableup = MAP(BEZIER(S2)([curve1a_tableup,curve1b_tableup]))(domain2)
map2_tableup = MAP(BEZIER(S2)([curve3a_tableup,curve3b_tableup]))(domain2)
map3_tableup = MAP(BEZIER(S2)([curve1a_tableup,curve2a_tableup,curve3a_tableup]))(domain2)
map4_tableup = MAP(BEZIER(S2)([curve1b_tableup,curve2b_tableup,curve3b_tableup]))(domain2)

#THE MODEL OF THE UP PART OF THE TABLE#
table_partup1 = map2_tableup
table_partup2 = STRUCT([map1_tableup,map3_tableup,map4_tableup])
table_partup = COLOR([1,0.843,0])(STRUCT([table_partup1,table_partup2])) 

#THE UP PART OF THE BASE#

#THE CURVES OF THE UP BASE#
curve1_baseup = BEZIER(S1)([[0,-0.45,0],[0.255,-0.085,0],[0.255,-0.085,0.85],[0,-0.35,0.85]])
curve2_baseup = BEZIER(S1)([[0.68,-0.45,0],[0.425,-0.085,0],[0.425,-0.085,0.85],[0.68,-0.35,0.85]])
curve3_baseup = BEZIER(S1)([[0,0.45,0],[0.255,0.085,0],[0.255,0.085,0.85],[0,0.45-0.1,0.85]])
curve4_baseup = BEZIER(S1)([[0.68,0.45,0],[0.425,0.085,0],[0.425,0.085,0.85],[0.68,0.45-0.1,0.85]])

#THE MAPS OF THE CURVES OF THE UP BASE#/
map1_baseup = MAP(BEZIER(S2)([curve1_baseup,curve2_baseup]))(domain2)
map2_baseup = MAP(BEZIER(S2)([curve3_baseup,curve4_baseup]))(domain2)
map3_baseup = MAP(BEZIER(S2)([curve1_baseup,curve3_baseup]))(domain2)
map4_baseup = MAP(BEZIER(S2)([curve2_baseup,curve4_baseup]))(domain2)

#THE BASEUP MODEL#
baseup = COLOR([0.329,0.329,0.329])(STRUCT([map1_baseup,map2_baseup,map3_baseup,map4_baseup]))

#THE DOWN PART OF THE BASE#/

#THE CURVES OF THE DOWN BASE#/
curve1_basedown = BEZIER(S1)([[-0.15,0,-0.1],[-0.15,0,-0.1],[0,0.2,-0.1],[0,0.2,0]])
curve2_basedown = BEZIER(S1)([[0.83,0,-0.1],[0.83,0,-0.1],[0.68,0.2,-0.1],[0.68,0.2,0]])
curve3_basedown = BEZIER(S1)([[-0.15,1.3,-0.1],[-0.15,1.3,-0.1],[0,1.1,-0.1],[0,1.1,0]])
curve4_basedown = BEZIER(S1)([[0.83,1.3,-0.1],[0.83,1.3,-0.1],[0.68,1.1,-0.1],[0.68,1.1,0]])

#THE MAPS OF THE CURVES OF THE DOWN BASE#/
map1_basedown = MAP(BEZIER(S2)([curve1_basedown,curve2_basedown]))(domain2)
map2_basedown = MAP(BEZIER(S2)([curve3_basedown,curve4_basedown]))(domain2)
map3_basedown = MAP(BEZIER(S2)([curve1_basedown,curve3_basedown]))(domain2)
map4_basedown = MAP(BEZIER(S2)([curve2_basedown,curve4_basedown]))(domain2)

#THE LITTLE BASE UNDER THE DOWN BASE#/

#THE CURVES OF THE LITTLE BASE#/
curve1_baselittle = BEZIER(S1)([[0-0.15,0,-0.1],[-0.18,-0.07,-0.125],[-0.18,-0.07,-0.2],[0-0.15,0,-0.2]])
curve2_baselittle = BEZIER(S1)([[0.83,0,-0.1],[0.86,-0.07,-0.125],[0.86,-0.07,-0.2],[0.83,0,-0.2]])
curve3_baselittle = BEZIER(S1)([[0.339,0,-0.1],[0.339,-0.05,-0.125],[0.339,-0.05,-0.2],[0.339,0,-0.2]])

curve4_baselittle = BEZIER(S1)([[-0.15,2.6,-0.1],[-0.18,2.67,-0.125],[-0.18,2.67,-0.2],[-0.15,2.6,-0.2]])
curve5_baselittle = BEZIER(S1)([[0.83,2.6,-0.1],[0.86,2.67,-0.125],[0.86,2.67,-0.2],[0.83,2.6,-0.2]])
curve6_baselittle = BEZIER(S1)([[0.339,2.6,-0.1],[0.339,2.65,-0.125],[0.339,2.65,-0.2],[0.339,2.6,-0.2]])
curve7_baselittle = BEZIER(S1)([[-0.15,1.3,-0.1],[-0.18,1.25,-0.125],[-0.18,1.25,-0.2],[-0.15,1.3,-0.2]])
curve8_baselittle = BEZIER(S1)([[0.83,1.3,-0.1],[0.86,1.25,-0.125],[0.86,1.25,-0.2],[0.83,1.3,-0.2]])
curve9_baselittle = BEZIER(S1)([[-0.15,0,-0.2],[0.83,0,-0.2]])
curve10_baselittle = BEZIER(S1)([[-0.15,2.6,-0.2],[0.83,2.6,-0.2]])

#THE MAPS OF THE LITTLE BASE#
map1_baselittle = MAP(BEZIER(S2)([curve1_baselittle,curve3_baselittle,curve2_baselittle]))(domain2)
map2_baselittle = MAP(BEZIER(S2)([curve4_baselittle,curve6_baselittle,curve5_baselittle]))(domain2)
map3_baselittle = MAP(BEZIER(S2)([curve1_baselittle,curve7_baselittle,curve4_baselittle]))(domain2)
map4_baselittle = MAP(BEZIER(S2)([curve2_baselittle,curve8_baselittle,curve5_baselittle]))(domain2)
map5_baselittle = MAP(BEZIER(S2)([curve9_baselittle,curve10_baselittle]))(domain2)

#THE MODEL OF THE LITTLE BASE#
baselittle = COLOR([0.329,0.329,0.329])(T([3])([-0.05])(T([2])([-0.65])(S([1,2,3])([1,0.5,0.5])
	(STRUCT([map1_baselittle,map2_baselittle,map3_baselittle,map4_baselittle,map5_baselittle])))))

# THE MODEL OF THE DOWN BASE#
basedown = T([2])([-0.65])(COLOR([0.835,0.839,0.713])(STRUCT([map1_basedown,map2_basedown,map3_basedown,map4_basedown,curve9_baselittle])))

# THE FINAL MODEL OF T24 BASE QUADRA#
t24basequadra_finalmodel = STRUCT([baseup,T([1])([0.3])(T([3])([0.85])(table_partup)),basedown,baselittle])
