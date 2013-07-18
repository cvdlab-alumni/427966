

def semicircle_a(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
	return semia

def semicircle_b(x1,y1,z,tx,ty,tz1,tz2):
	semix = float(x1)/2
	semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
	return semib

def SEMISPHERE(radius):

  def SPHERE0(subds):
    N , M = subds
    domain = PROD([INTERVALS(PI)(N),INTERVALS(2*PI)(M)])
    fx  = lambda p: radius * math.cos(p[0])  * math.sin (p[1])
    fy  = lambda p: radius * math.cos(p[0]) * math.cos(p[1])
    fz  = lambda p: radius * math.sin(p[0]) 
    ret=  MAP([fx, fy, fz])(domain)
    return ret
  return SPHERE0

domain1 = INTERVALS(1)(32);
domain2 =  PROD([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)
color_green = [0.133,0.545,0.133]
color_light = [0.2392,0.2392,0.2392]

###################################################LP26B ONDA#####################################################

#THE LAMP STRUCTURE#

#THE CURVES OF THE STRUCTURE#
curve1_lamp = BEZIER(S1)([[0,0,0],[1,0,0],[3,3,0],[4,3,0],[4,0,0],[4.5,0,0]])
curve2_lamp = BEZIER(S1)([[-2,0,-0.1],[-2,0,0],[0,0,0]])
curve3_lamp = BEZIER(S1)([[4.5,0,0],[5.5,0,0],[5.5,0,-0.1]])
curve4_lamp = BEZIER(S1)([[0,0,-1.5],[1,0,-1.5],[3,3,-1.5],[4,3,-1.5],[4,0,-1.5],[4.5,0,-1.5]])
curve5_lamp = BEZIER(S1)([[-2,0,-1.4],[-2,0,-1.5],[0,0,-1.5]])
curve6_lamp = BEZIER(S1)([[4.5,0,-1.5],[5.5,0,-1.5],[5.5,0,-1.4]])
curve7_lamp = BEZIER(S1)([[0,-0.15,0],[1,-0.15,0],[3,2.85,0],[4,2.85,0],[3.9,-0.15,0],[4.5,-0.15,0]])
curve8_lamp = BEZIER(S1)([[-2,-0.15,-0.1],[-2,-0.15,0],[0,-0.15,0]])
curve9_lamp = BEZIER(S1)([[4.5,-0.15,0],[5.5,-0.15,0],[5.5,-0.15,-0.1]])
curve10_lamp = BEZIER(S1)([[0,-0.15,-1.5],[1,-0.15,-1.5],[3,2.85,-1.5],[4,2.85,-1.5],[3.9,-0.15,-1.5],[4.5,-0.15,-1.5]])
curve11_lamp = BEZIER(S1)([[-2,-0.15,-1.4],[-2,-0.15,-1.5],[0,-0.15,-1.5]])
curve12_lamp = BEZIER(S1)([[4.5,-0.15,-1.5],[5.5,-0.15,-1.5],[5.5,-0.15,-1.4]])


#THE MAPS OF THE STRUCTURE#
map1_lamp = MAP(BEZIER(S2)([curve1_lamp,curve4_lamp]))(domain2)
map2_lamp = MAP(BEZIER(S2)([curve2_lamp,curve5_lamp]))(domain2)
map3_lamp = MAP(BEZIER(S2)([curve3_lamp,curve6_lamp]))(domain2)
map4_lamp = MAP(BEZIER(S2)([curve4_lamp,curve10_lamp]))(domain2)
map5_lamp = MAP(BEZIER(S2)([curve5_lamp,curve11_lamp]))(domain2)
map6_lamp = MAP(BEZIER(S2)([curve6_lamp,curve12_lamp]))(domain2)
map7_lamp = MAP(BEZIER(S2)([curve1_lamp,curve7_lamp]))(domain2)
map8_lamp = MAP(BEZIER(S2)([curve2_lamp,curve8_lamp]))(domain2)
map9_lamp = MAP(BEZIER(S2)([curve3_lamp,curve9_lamp]))(domain2)
map10_lamp = MAP(BEZIER(S2)([curve10_lamp,curve7_lamp]))(domain2)
map11_lamp = MAP(BEZIER(S2)([curve11_lamp,curve8_lamp]))(domain2)
map12_lamp = MAP(BEZIER(S2)([curve12_lamp,curve9_lamp]))(domain2)

#THE MODEL OF THE STRUCTURE#
lamp_structure = COLOR([0.18,0.545,0.341])(S([1,2,3])([0.8,1,1.2])(STRUCT([map1_lamp,map2_lamp,map3_lamp,map4_lamp,map5_lamp,map6_lamp,
  map7_lamp,map8_lamp,map9_lamp,map10_lamp,map11_lamp,map12_lamp])))

#####################################################THE BULB############################################

#THE CURVES OF THE BULB#
curve1a_light = semicircle_a(1.2,0.85,0.1,0,0,0,0)
curve1b_light = semicircle_b(1.2,0.85,0.1,0,0,0,0)
curve2a_light = semicircle_a(1.2,0.85,0.15,0,0,0,0)
curve2b_light = semicircle_b(1.2,0.85,0.15,0,0,0,0)
curve3a_light = semicircle_a(1.1,0.75,0.15,0,0,0,0)
curve3b_light = semicircle_b(1.1,0.75,0.15,0,0,0,0)
curve4a_light = semicircle_a(1.1,0.75,0.9,0,0,0,0)
curve4b_light = semicircle_b(1.1,0.75,0.9,0,0,0,0)
curve5a_light = semicircle_a(0.6,0.4,1.1,0,0,0,0)
curve5b_light = semicircle_b(0.6,0.4,1.1,0,0,0,0)
curve6a_light = semicircle_a(0.6,0.4,1.5,0,0,0,0)
curve6b_light = semicircle_b(0.6,0.4,1.5,0,0,0,0)
curve7a_light = semicircle_a(0.3,0.2,1.5,0,0,0,0)
curve7b_light = semicircle_b(0.3,0.2,1.5,0,0,0,0)
curve8a_light = semicircle_a(0.2,0.15,1.65,0,0,0,0)
curve8b_light = semicircle_b(0.2,0.15,1.65,0,0,0,0)

#THE MAPS OF THE BULB#
map1_light = COLOR([1,1,0])(MAP(BEZIER(S2)([curve1a_light,curve1b_light]))(domaininv))
map2_light = COLOR(color_light)(MAP(BEZIER(S2)([curve2a_light,curve2b_light]))(domain2))
map3_light = COLOR(color_light)(MAP(BEZIER(S2)([curve1a_light,curve2a_light]))(domain2))
map4_light = COLOR(color_light)(MAP(BEZIER(S2)([curve1b_light,curve2b_light]))(domain2))
map5_light =  COLOR(color_light)(MAP(BEZIER(S2)([curve3a_light,curve3b_light]))(domain2))
map6_light =  COLOR(color_light)(MAP(BEZIER(S2)([curve3a_light,curve4a_light,curve5a_light]))(domain2))
map7_light =  COLOR(color_light)(MAP(BEZIER(S2)([curve3b_light,curve4b_light,curve5b_light]))(domain2))
map8_light = MAP(BEZIER(S2)([curve5a_light,curve5b_light]))(domain2)
map9_light = MAP(BEZIER(S2)([curve5a_light,curve6a_light]))(domain2)
map10_light = MAP(BEZIER(S2)([curve5b_light,curve6b_light]))(domain2)
map11_light = MAP(BEZIER(S2)([curve6a_light,curve6b_light]))(domain2)
map12_light =  COLOR([0.3294,0.3294,0.3294])(MAP(BEZIER(S2)([curve7a_light,curve8a_light]))(domain2))
map13_light =  COLOR([0.3294,0.3294,0.3294])(MAP(BEZIER(S2)([curve7b_light,curve8b_light]))(domain2))
map14_light = COLOR([0.3294,0.3294,0.3294])(MAP(BEZIER(S2)([curve8a_light,curve8b_light]))(domain2))

#THE MODEL OF THE BULB#
light = T([1])([1.4])(T([2])([1.35])(T([3])([-0.85])(R([1,2])(-PI/3*2.3/3)(R([1,3])(-PI/2)(STRUCT([map1_light,map2_light,map3_light,map4_light,
  map5_light,map6_light,map7_light,map8_light,map9_light,map10_light,map11_light,map12_light,map13_light,map14_light]))))))

#THE GLASS#
curve1a_glass = semicircle_a(1.2,0.85,0.1,0,0,0,0)
curve1b_glass = semicircle_b(1.2,0.85,0.1,0,0,0,0)
curve2a_glass = semicircle_a(0,0,0.3,0,0,0,0)
curve2b_glass = semicircle_b(0,0,0.3,0,0,0,0)
glass_light = COLOR([1,1,1])(R([1,2])(PI/4)(R([2,3])(-PI/2)(T([1])([1.95])(T([2])([0.85])(T([3])([-0.25])(SEMISPHERE(0.64)([16,16])))))));

#THE STUDS#
stud = SEMISPHERE(0.1)([16,16])
studs = R([2,3])(-PI/2)(T([2])([0.85])(T([3])([0])(STRUCT([T([1])([-0.85])(stud),T([1])([3.9])(stud)]))))

#########################################################THE LP26B ONDA MODEL##################################################
lp26bonda = STRUCT([light,lamp_structure,glass_light,studs])
