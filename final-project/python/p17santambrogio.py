
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
color_green = [0.133,0.545,0.133]

################################################################P17 SANT AMBROGIO#####################################################

###############################################################THE SIDES OF THE SOFA##################################################

#THE CURVES OF THE SIDES#
curve1_sideleft = BEZIER(S1)([[0.5,0.2,0],[-0.3,0.2,0],[-1.7,0.2,0],[-1.7,0,0],[-2.3,-0.6,0],[-2.7,-3,0],[-3.3,-3.3,0]]) 
curve2_sideleft = BEZIER(S1)([[-3.3,-3.3,0],[-6,-3.3,0],[-8.9,-3.4,0]]) 
curve3_sideleft = BEZIER(S1)([[-8.9,-3.4,0],[-9.4,-3.7,0],[-9.4,-4.6,0],[-9.4,-6.9,0]]) 
curve4_sideleft = BEZIER(S1)([[-9.4,-6.9,0],[-9.1,-7.2,0],[-8.6,-7.2,0],[0.2,-7.2,0]]) 
curve5_sideleft = BEZIER(S1)([[0.2,-7.2,0],[0.7,-7.2,0],[0.7,-6.9,0],[0.7,0,0]])
curve6_sideleft = BEZIER(S1)([[0.7,0,0],[0.7,0.2,0],[0.5,0.2,0]])
curve7_sideleft = BEZIER(S1)([[0.5,0.2,-1],[-0.3,0.2,-1],[-1.7,0.2,-1],[-1.7,0,-1],[-2.3,-0.6,-1],[-2.7,-3,-1],[-3.3,-3.3,-1]]) 
curve8_sideleft = BEZIER(S1)([[-3.3,-3.3,-1],[-6,-3.3,-1],[-8.9,-3.4,-1]]) 
curve9_sideleft = BEZIER(S1)([[-8.9,-3.4,-1],[-9.4,-3.7,-1],[-9.4,-4.6,-1],[-9.4,-6.9,-1]]) 
curve10_sideleft = BEZIER(S1)([[-9.4,-6.9,-1],[-9.1,-7.2,-1],[-8.6,-7.2,-1],[0.2,-7.2,-1]]) 
curve11_sideleft = BEZIER(S1)([[0.2,-7.2,-1],[0.7,-7.2,-1],[0.7,-6.9,-1],[0.7,0,-1]])
curve12_sideleft = BEZIER(S1)([[0.7,0,-1],[0.7,0.2,-1],[0.5,0.2,-1]])
curve13_sideleft = BEZIER(S1)([[0.6,0.4,-0.5],[-0.3,0.4,-0.5],[-1.7,0.4,-0.5],[-1.7,0,-0.5],[-2.5,-0.6,-0.5],[-2.9,-2.7,-0.5],[-3.5,-3,-0.5]]) 
curve14_sideleft = BEZIER(S1)([[-3.5,-3,-0.5],[-6,-3,-0.5],[-8.1,-3.1,-0.5]]) 
curve15_sideleft = BEZIER(S1)([[-8.1,-3.1,-0.5],[-9.6,-3.2,-0.5],[-9.6,-4.6,-0.5],[-9.6,-6.9,-0.5]]) 
curve16_sideleft = BEZIER(S1)([[-9.6,-6.9,-0.5],[-9.1,-7.2,-0.5],[-8.6,-7.2,-0.5],[0.3,-7.2,-0.5]]) 
curve17_sideleft = BEZIER(S1)([[0.3,-7.2,-0.5],[0.8,-7.2,-0.5],[0.8,-6.9,-0.5],[0.8,0,-0.5]])
curve18_sideleft = BEZIER(S1)([[0.8,0,-0.5],[0.8,0.2,-0.5],[0.6,0.4,-0.5]])
curvefull1_sideleft = BEZIER(S1)([[0.7,-3.2,0],[0.7,-6.9,0],[0.7,-7.2,0],[0.15,-7.2,0]])
curvefull2_sideleft = BEZIER(S1)([[-9.4,-6.9,0],[-9.1,-7.2,0],[-8.6,-7.2,0],[-3,-7.2,0]])
curvefull3_sideleft = BEZIER(S1)([[0.2,-7.2,0],[-5,-7.2,0]])
curvefull4_sideleft = BEZIER(S1)([[0.5,0.2,0],[0.7,0.2,0],[0.7,0,0]])
curvefull5_sideleft = BEZIER(S1)([[0.7,0,0],[0.7,-4,0]])

#THE MAPS OF THE SIDES#
map1_sideleft = MAP(BEZIER(S2)([curve1_sideleft,curve13_sideleft,curve7_sideleft]))(domaininv)
map2_sideleft = MAP(BEZIER(S2)([curve2_sideleft,curve14_sideleft,curve8_sideleft]))(domaininv)
map3_sideleft = MAP(BEZIER(S2)([curve3_sideleft,curve15_sideleft,curve9_sideleft]))(domaininv)
map4_sideleft = MAP(BEZIER(S2)([curve4_sideleft,curve16_sideleft,curve10_sideleft]))(domaininv)
map5_sideleft = MAP(BEZIER(S2)([curve5_sideleft,curve17_sideleft,curve11_sideleft]))(domaininv)
map6_sideleft = MAP(BEZIER(S2)([curve6_sideleft,curve18_sideleft,curve12_sideleft]))(domaininv)
map7_sideleft = MAP(BEZIER(S2)([curve3_sideleft,curvefull1_sideleft]))(domaininv)
map8_sideleft = MAP(BEZIER(S2)([curve2_sideleft,curvefull2_sideleft]))(domaininv)
map9_sideleft = MAP(BEZIER(S2)([curve1_sideleft,curvefull3_sideleft]))(domaininv)
map10_sideleft = MAP(BEZIER(S2)([curve1_sideleft,curvefull4_sideleft]))(domaininv)
map11_sideleft = MAP(BEZIER(S2)([curve1_sideleft,curvefull5_sideleft]))(domaininv)

#THE MODEL OF THE SIDES#
close_sideleft = STRUCT([map7_sideleft,map8_sideleft,map9_sideleft,map10_sideleft,map11_sideleft])
sideleft = S([1,2,3])([1,1.2,1])(STRUCT([map1_sideleft,map2_sideleft,map3_sideleft,map4_sideleft,map5_sideleft,map6_sideleft,
  close_sideleft,T([3])([-1])(close_sideleft)]))
sideright = T([3])([-12])(sideleft)
sides = STRUCT([sideleft,sideright])

#############################################THE BACKREST OF THE SOFA###############################################

#THE CURVES OF THE BACKREST#
curve1_backrest = BEZIER(S1)([[0.2,-7.2,-12],[0.7,-7.2,-12],[0.7,-6.9,-12],[0.7,0,-12]])
curve2_backrest = BEZIER(S1)([[0.69,-0.05,-1],[0.69,-0.05,-12]])
curve3_backrest = BEZIER(S1)([[0.235,0.35,-1],[0.235,0.35,-12]])
curve4_backrest = BEZIER(S1)([[-0.2,0,-1],[-0.2,0,-12]])
curve5_backrest = BEZIER(S1)([[-0.2,-7.2,-1],[-0.2,-7.2,-12]])
curve6_backrest = BEZIER(S1)([[-9.4,-6.9,-12],[-9.1,-7.2,-12],[-8.6,-7.2,-12],[0.2,-7.2,-12]])
curve7_backrest = BEZIER(S1)([[-0.2,-5.1,-12],[-9.2,-5.1,-12],[-9.4,-5.1,-12],[-9.4,-6.9,-12]]) 
curve8_backrest = BEZIER(S1)([[-0.2,-5.1,-1],[-9.2,-5.1,-1],[-9.4,-5.1,-1],[-9.4,-6.9,-1]]) 

#THE MAPS OF THE BACKREST#
map1_backrest = S([1,2,3])([1,1.2,1])(MAP(BEZIER(S2)([curve5_sideleft,curve1_backrest]))(domaininv))
map2_backrest = S([1,2,3])([1,1.2,1])(MAP(BEZIER(S2)([curve2_backrest,curve3_backrest,curve4_backrest]))(domaininv))
map3_backrest = S([1,2,3])([1,1.2,1])(MAP(BEZIER(S2)([curve6_backrest,curve4_sideleft]))(domaininv))
map4_backrest = S([1,2,3])([1,1.2,1])(MAP(BEZIER(S2)([curve5_backrest,curve4_backrest]))(domain2))
map5_backrest = S([1,2,3])([1,1.2,1])(MAP(BEZIER(S2)([curve7_backrest,curve8_backrest]))(domain2))

#THE MODEL OF THE BACKREST#
backrest = STRUCT([map1_backrest,map2_backrest,map3_backrest,map4_backrest,map5_backrest])

#THE MODEL OF THE SOFA STRUCTURE#
sofa_structure = S([1,2,3])([0.7,0.8,1])(STRUCT([sides,backrest]))

#######################################################THE PILLOWS#####################################################

#THE CURVES OF THE PILLOWS#
curve1_littlepillow = BEZIER(S1)([[2.7,0,0], [2.7,0.3,0],[-2.7,0.3,0],[-2.7,0,0]])
curve2_littlepillow = BEZIER(S1)([[2.7,-3,0],[2.7,-3.3,0],[-2.7,-3.3,0],[-2.7,-3,0]])
curve3_littlepillow = BEZIER(S1)([[2.7,0,-1],[2.7,0.3,-1],[-2.7,0.3,-1],[-2.7,0,-1]])
curve4_littlepillow = BEZIER(S1)([[2.7,-3,-1],[2.7,-3.3,-1],[-2.7,-3.3,-1],[-2.7,-3,-1]])
curve5_littlepillow = BEZIER(S1)([[2.7,0,0],[2.7,-3,0]])
curve6_littlepillow = BEZIER(S1)([[2.7,0,-1],[2.7,-3,-1]])
curve7_littlepillow = BEZIER(S1)([[-2.7,0,0],[-2.7,-3,0]])
curve8_littlepillow = BEZIER(S1)([[-2.7,0,-1],[-2.7,-3,-1]])
curve9_littlepillow = BEZIER(S1)([[2.7,-2,0.3],[-2.7,-2,0.3]])

#THE MAPS OF THE PILLOWS#
map1_littlepillow = MAP(BEZIER(S2)([curve1_littlepillow,curve9_littlepillow,curve2_littlepillow]))(domaininv)
map2_littlepillow = MAP(BEZIER(S2)([curve3_littlepillow,curve4_littlepillow]))(domaininv)
map3_littlepillow = MAP(BEZIER(S2)([curve1_littlepillow,curve3_littlepillow]))(domaininv)
map4_littlepillow = MAP(BEZIER(S2)([curve2_littlepillow,curve4_littlepillow]))(domaininv)
map5_littlepillow = MAP(BEZIER(S2)([curve5_littlepillow,curve6_littlepillow]))(domaininv)
map6_littlepillow = MAP(BEZIER(S2)([curve7_littlepillow,curve8_littlepillow]))(domaininv)

#THE MODEL OF THE PILLOWS#
littlepillow1 = T([2])([-1])(T([1])([-0.3])(T([3])([-3.8])(R([1,2])(-PI/8)(R([1,3])(-PI/2)(STRUCT([map1_littlepillow,map2_littlepillow,
  map3_littlepillow,map4_littlepillow,map5_littlepillow,map6_littlepillow]))))))
littlepillow2 = T([3])([-5.45])(littlepillow1)
bigpillow1 = T([2])([-5])(S([1,2,3])([1.4,1,1])(R([1,2])(-3*PI/8)(littlepillow1)))
bigpillow2 = T([3])([-5.45])(bigpillow1)
pillows = STRUCT([littlepillow1,littlepillow2,bigpillow1,bigpillow2])

###################################################THE P17 SANTAMBROGIO MODEL######################################################
p17santambrogiomodel = COLOR(color_green)(STRUCT([pillows,sofa_structure]))

