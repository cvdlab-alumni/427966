
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

#######################################THE FUNNEL#################################
curve1a_funnel = semicircle_a(3,2,0,0,0,0,0)
curve1b_funnel = semicircle_b(3,2,0,0,0,0,0)
curve2a_funnel = semicircle_a(0.45,0.28,3,0,0,0,0)
curve2b_funnel = semicircle_b(0.45,0.28,3,0,0,0,0)
curve3a_funnel = semicircle_a(0.2,0.15,3.1,0,0,0,0)
curve3b_funnel = semicircle_b(0.2,0.15,3.1,0,0,0,0)

map1_funnel = MAP(BEZIER(S2)([curve1a_funnel,curve2a_funnel]))(domain2)
map2_funnel = MAP(BEZIER(S2)([curve1b_funnel,curve2b_funnel]))(domain2)
map3_funnel = MAP(BEZIER(S2)([curve2a_funnel,curve3a_funnel]))(domain2)
map4_funnel = MAP(BEZIER(S2)([curve2b_funnel,curve3b_funnel]))(domain2)
map5_funnel = MAP(BEZIER(S2)([curve3a_funnel,curve3b_funnel]))(domain2)

funnel = COLOR([0.05,0.05,0.05])(STRUCT([map1_funnel,map2_funnel,map3_funnel,map4_funnel,map5_funnel]))
#################################################BODY AND BASE##################################
curve1a_body = semicircle_a(0.2,0.15,18,0,0,0,0)
curve1b_body = semicircle_b(0.2,0.15,18,0,0,0,0)
curve2a_body = semicircle_a(2.2,1.3,18,0,0,0,0)
curve2b_body = semicircle_b(2.2,1.3,18,0,0,0,0)
curve3a_body = semicircle_a(2.2,1.3,18.3,0,0,0,0)
curve3b_body = semicircle_b(2.2,1.3,18.3,0,0,0,0)

map1_body = COLOR([1,0.7568,0.145])(MAP(BEZIER(S2)([curve3a_funnel,curve1a_body]))(domain2))
map2_body = COLOR([1,0.7568,0.145])(MAP(BEZIER(S2)([curve3b_funnel,curve1b_body]))(domain2))
map3_body = COLOR([0.05,0.05,0.05])(MAP(BEZIER(S2)([curve2a_body,curve2b_body]))(domain2))
map4_body = COLOR([0.05,0.05,0.05])(MAP(BEZIER(S2)([curve3a_body,curve3b_body]))(domain2))
map5_body = COLOR([0.05,0.05,0.05])(MAP(BEZIER(S2)([curve2a_body,curve3a_body]))(domain2))
map6_body = COLOR([0.05,0.05,0.05])(MAP(BEZIER(S2)([curve2b_body,curve3b_body]))(domain2))
body = STRUCT([map1_body,map2_body,map3_body,map4_body,map5_body,map6_body])

#THE BULB#
bulb = COLOR([1,1,0])(T([3])([1.7])(T([2])([0])(R([2,3])(PI)(SEMISPHERE(0.5)([16,16])))));

#######################################LTE5 IMBUTO MODEL#####################################
lte5imbuto_model = STRUCT([funnel,body,bulb]) 
