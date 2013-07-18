

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
################################################T20 FASCIA SPECCHIATA##########################################à

###############################################THE LEGS OF THE TABLE####################################################à

#THE CURVES OF THE LEGS#
curve_leg1 = BEZIER(S1)([[0.3,0,0],[0,0,0],[-0.5,0.9,0],[0.5,1.5,0],[0.8,1.3,0],[1.5,1,0],[1.3,0,0],[1,0,0]])
curve_leg2 = BEZIER(S1)([[0.3,0,0.7],[0,0,0.7],[-0.5,0.9,0.7],[0.5,1.5,0.7],[0.8,1.3,0.7],[1.5,1,0.7],[1.3,0,0.5],[1,0,0.7]])
curve_leg3 = BEZIER(S1)([[0.2,0+0.03,0],[0.3,0+0.03,0],[-0.05,0+0.03,0],[-0.6,0.9+0.03,0],[0.5,1.5+0.03,0],[0.8,1.3+0.03,0],
	[1.6,0.95+0.03,0],[1.3,0+0.03,0],[1,0+0.03,0]])
curve_leg4 = BEZIER(S1)([[0.2,0+0.03,0.7],[0.3,0+0.03,0.7],[-0.05,0+0.03,0.7],[-0.6,0.9+0.03,0.7],[0.5,1.5+0.03,0.7],[0.8,1.3+0.03,0.7],
	[1.6,0.95+0.03,0.7],[1.3,0+0.03,0.7],[1,0+0.03,0.7]])

#THE MAPS OF THE LEGS#
map1_leg = MAP(BEZIER(S2)([curve_leg1,curve_leg2]))(domain2)
map2_leg = MAP(BEZIER(S2)([curve_leg3,curve_leg4]))(domain2)
map3_leg = MAP(BEZIER(S2)([curve_leg1,curve_leg3]))(domain2)
map4_leg = MAP(BEZIER(S2)([curve_leg2,curve_leg4]))(domain2)

#THE MODEL OF THE LEGS#
leg1 = COLOR([0.129,0.129,0.129])(STRUCT([map1_leg,map2_leg,map3_leg,map4_leg]))
leg2 = T([1])([0.7])(T([2])([0.5])(R([1,2])(PI)(leg1)))
legs = STRUCT([leg1,leg2])

#################################################THE UP PART OF THE TABLE##########################################################

#THE CURVES OF THE UP PART#
curve_table1a = semicircle_a(2.3,1.5,0,0,0,0,0)
curve_table1b = semicircle_b(2.3,1.5,0,0,0,0,0)
curve_table2a = semicircle_a(2.3,1.5,0.03,0,0,0,0)
curve_table2b = semicircle_b(2.3,1.5,0.03,0,0,0,0)
curve_table3a = semicircle_a(2.8,1.9,0,0,0,0,0)
curve_table3b = semicircle_b(2.8,1.9,0,0,0,0,0)
curve_table4a = semicircle_a(2.8,1.9,0.03,0,0,0,0)
curve_table4b = semicircle_b(2.8,1.9,0.03,0,0,0,0)

#THE MAPS OF THE UP PART#
map1_tableup = MAP(BEZIER(S2)([curve_table1a,curve_table1b]))(domain2)
map2_tableup = MAP(BEZIER(S2)([curve_table2a,curve_table2b]))(domain2)
map3_tableup = MAP(BEZIER(S2)([curve_table1a,curve_table2a]))(domain2)
map4_tableup = MAP(BEZIER(S2)([curve_table1b,curve_table2b]))(domain2)
map5_tableup = MAP(BEZIER(S2)([curve_table1a,curve_table3a]))(domain2)
map6_tableup = MAP(BEZIER(S2)([curve_table1b,curve_table3b]))(domain2)
map7_tableup = MAP(BEZIER(S2)([curve_table2a,curve_table4a]))(domain2)
map8_tableup = MAP(BEZIER(S2)([curve_table2b,curve_table4b]))(domain2)
map9_tableup = MAP(BEZIER(S2)([curve_table3a,curve_table4a]))(domain2)
map10_tableup = MAP(BEZIER(S2)([curve_table3b,curve_table4b]))(domain2)

#THE MODEL OF THE UP PART#
def table_traslation(object): 
 return T([2])([0.25])(T([1])([0.3])(T([3])([0.7])(object))) 

table1_up = COLOR([1,1,1,0.7])(table_traslation(STRUCT([map1_tableup,map2_tableup,map3_tableup,map4_tableup])))
table2_up = COLOR([0.623,0.713,0.8,1])(table_traslation(STRUCT([map5_tableup,map6_tableup,map7_tableup,map8_tableup,map9_tableup,map10_tableup])))
table_up = STRUCT([table1_up,table2_up])

#######################################THE FINAL MODEL OF T20 FASCIA SPECCHIATA###################################################àà
t20_fascia_specchiata = STRUCT([table_up,legs])
