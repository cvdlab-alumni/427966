
from pyplasm import *
import scipy
from scipy import *

#---------------------------------------------------------
def VERTEXTRUDE((V,coords)):
    """
        Utility function to generate the output model vertices in a 
        multiple extrusion of a LAR model.
        V is a list of d-vertices (each given as a list of d coordinates).
        coords is a list of absolute translation parameters to be applied to 
        V in order to generate the output vertices.
        
        Return a new list of (d+1)-vertices.
    """
    return CAT(AA(COMP([AA(AR),DISTR]))(DISTL([V,coords])))

def cumsum(iterable):
    # cumulative addition: list(cumsum(range(4))) => [0, 1, 3, 6]
    iterable = iter(iterable)
    s = iterable.next()
    yield s
    for c in iterable:
        s = s + c
        yield s

def larExtrude(model,pattern):
    V,FV = model
    d = len(FV[0])
    offset = len(V)
    m = len(pattern)
    outcells = []
    for cell in FV:
        # create the indices of vertices in the cell "tube"
        tube = [v + k*offset for k in range(m+1) for v in cell]
        # take groups of d+1 elements, via shifting by one
        rangelimit = len(tube)-d
        cellTube = [tube[k:k+d+1] for k in range(rangelimit)]
        outcells += [scipy.reshape(cellTube,newshape=(m,d,d+1)).tolist()]
    outcells = AA(CAT)(TRANS(outcells))
    outcells = [group for k,group in enumerate(outcells) if pattern[k]>0 ]
    coords = list(cumsum([0]+(AA(ABS)(pattern))))
    outVerts = VERTEXTRUDE((V,coords))
    newModel = outVerts, CAT(outcells)
    return newModel

def GRID(args):
    model = ([[]],[[0]])
    for k,steps in enumerate(args):
        model = larExtrude(model,steps*[1])
    V,cells = model
    verts = AA(list)(scipy.array(V) / AA(float)(args))
    return MKPOL([verts, AA(AA(lambda h:h+1))(cells), None])
def semicircle_a(x1,y1,z,tx,ty,tz1,tz2):
    semix = float(x1)/2
    semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
    return semia

def semicircle_b(x1,y1,z,tx,ty,tz1,tz2):
    semix = float(x1)/2
    semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
    return semib





#the skeleton of the car for mounting the wheels

domain1D = GRID([10]);
domain2D = GRID([10,10])
domain1 = domain2D
domaininv = MAP([S2,S1])(domain1)


ControlPoints = [[-12.8,0],[-6,0],[-6,0],[-6,3],[-2,3],[-2,0],[-2,0],[11,0],[11,0],[11,3],
                 [15,3],[15,0],[15,0],[18,1],[19,1.5],[19,2.5],[19,2.5],[18,2.5],[18,2.5],[18,3.5],
                 [18,3.5],[18.5,3.5],[18.5,3.5],[18.5,4]]
lateral_down = NUBSPLINE(3)([0,0,0,0, 1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,20,21,21,21,21])(ControlPoints)

ControlPoints2 = [[18.5,4],[17.5,4],[17.5,4],[11,6.5],[11,6.5],[10.8,6.8],[10.8,6.8],[7,7.5],[3,7.5],[3,7.5]
                ,[-3,5],[-3,5],[-3.8,5],[-8,4.5],[-9.5,4],[-9.5,4],[-13,3.3],[-13,3.3],[-13,3],[-13,3],
                [-13,1.7],[-13,1.7],[-12.5,1.4],[-12.8,0.9],[-12.8,0.9],[-12.8,0.9],[-12.8,0],[-12.8,0],[-12.8,0],[-12.8,0]]

lateral_up = NUBSPLINE(3)([0,0,0,0,1,2,3,4,5,6,   7,8,9,10,11,12,13,14,15,16,    17,18,19,20,21,22,23,24,25,26,27,27,27,27])(ControlPoints2)
lateralSection = T([2,1])(-4)(T([1,2])(-4)(STRUCT([lateral_down,lateral_up])))



upsec1 = BEZIER(S1)([[0,0,0],[0.4,0,0.5],[4.8,0,0.5],[7,0,0.3]])
upsec2 = BEZIER(S1)([[0,0,0],[-0.5,0,-0.5],[-0.5,0,-8],[0,0,-8]])
upsec3 = BEZIER(S1)([[7,0,0.3],[8.5,0,0.3]])
upsec4 = BEZIER(S1)([[8.5,0,0.3],[10.5,0,0.4]])
upsec5 = BEZIER(S1)([[10.5,0,0.4],[16,0,1],[17,0,0.8]])
upsec6 = BEZIER(S1)([[17,0,0.8],[17,0,0.75],[19,0,0.75],[19,0,0.8]])
upsec7 = BEZIER(S1)([[19,0,0.8],[22,0,1.2]])
upsec8 = BEZIER(S1)([[22,0,1.2],[22.8,0,1.2],[22.8,0,-9.2],[22,0,-9.2],[22,0,-9.2]])
upmap1 = MAP(BEZIER(S2)([upsec1]))(domain2D)
upmap2 = MAP(BEZIER(S2)([upsec2]))(domain2D)
upmap3 = MAP(BEZIER(S2)([upsec3]))(domain2D)
upmap4 = MAP(BEZIER(S2)([upsec4]))(domain2D)
upmap5 = MAP(BEZIER(S2)([upsec5]))(domain2D)
upmap6 = MAP(BEZIER(S2)([upsec6]))(domain2D)
upmap7 = MAP(BEZIER(S2)([upsec7]))(domain2D)
upmap8 = MAP(BEZIER(S2)([upsec8]))(domain2D)

uplateral = STRUCT([upmap1,upmap3,upmap4,upmap5,upmap6,upmap7])
upSection = T([3,1])(4)(T([1,3])(-12)(STRUCT([uplateral,T([3,1])(-8)(R([2,3])(PI)(uplateral)),upmap2,upmap8])))

backsec1 = BEZIER(S1)([[0,0,-0.3],[0,-1,-0.3],[0,-2,-0.3],[0,-2,-0.3],[0,-2,6],[0,-2,6],[0,-1,6],[0,0,6]])
backsec2 = BEZIER(S1)([[0,0,6],[0,0,6]])
backsec3 = BEZIER(S1)([[0,0,6],[0,0.15,5.4]])
backsec4 = BEZIER(S1)([[0,0.15,5.4],[0,0.8,5.2]])
backsec5 = BEZIER(S1)([[0,0.8,5.2],[0,1.2,5],[0,1.2,5],[0,1.2,0.5],[0,1.2,0.5],[0,0.8,0.5],[0,0.15,0.3]])
backsec6 = BEZIER(S1)([[0,0.15,0.3],[0,0,-0.3]])


backmap1 = MAP(BEZIER(S2)([backsec1]))(domain2D)
backmap2 = MAP(BEZIER(S2)([backsec2]))(domain2D)
backmap3 = MAP(BEZIER(S2)([backsec3]))(domain2D)
backmap4 = MAP(BEZIER(S2)([backsec4]))(domain2D)
backmap5 = MAP(BEZIER(S2)([backsec5]))(domain2D)

backmap6 = MAP(BEZIER(S2)([backsec6]))(domain2D)
backSection = T([2,1])(0.5)(T([3,1])(-2.7)(STRUCT([backmap1,backmap2,backmap3,backmap4,backmap5,backmap6])))

skeleton = STRUCT([S([1,2,3])([1.38,1,1])(upSection),lateralSection,S([1,2,3])([1.7,1.7,1.7])(backSection)])


#wheels part

wheel1a = semicircle_a(1.8,1.2,0,0,0,0,0)
wheel1b = semicircle_b(1.8,1.2,0,0,0,0,0)

wheel2a = semicircle_a(1.5,1,0,0,0,0,0) 
wheel2b = semicircle_b(1.5,1,0,0,0,0,0)

wheel3a = semicircle_a(1.8,1.2,1,0,0,0,0)
wheel3b = semicircle_b(1.8,1.2,1,0,0,0,0)

wheel4a = semicircle_a(1.5,1,1,0,0,0,0) 
wheel4b = semicircle_b(1.5,1,1,0,0,0,0)

def rim_star(z,shadow,tz):
    domain1 = GRID([10,10])
    domaininv = MAP([S2,S1])(GRID([10,10]))

    d = domain1
    if shadow == 1:
        domain1 = domaininv
        domaininv = d
    
    rim1a = semicircle_a(0.5,0.35,z,0,0,0,0)
    rim1b = semicircle_b(0.5,0.35,z,0,0,0,0)
    rimDouble1a = semicircle_a(0.5,0.35,z-tz,0,0,0,0)
    rimDouble1b = semicircle_b(0.5,0.35,z-tz,0,0,0,0)

    rim2a = semicircle_a(0.3,0.2,z,0,0,0,0)
    rim2b = semicircle_b(0.3,0.2,z,0,0,0,0)
    rimDouble2a = semicircle_a(0.3,0.2,z-tz,0,0,0,0)
    rimDouble2b = semicircle_b(0.3,0.2,z-tz,0,0,0,0)    
    
    rim3a = semicircle_a(1.5,1,z,0,0,0,0) 
    rim3b = semicircle_b(1.5,1,z,0,0,0,0)
    rimDouble3a = semicircle_a(1.5,1,z-tz,0,0,0,0) 
    rimDouble3b = semicircle_b(1.5,1,z-tz,0,0,0,0)
    
    rim4a = semicircle_a(1.3,0.8,z,0,0,0,0) 
    rim4b = semicircle_b(1.3,0.8,z,0,0,0,0)
    rimDouble4a = semicircle_a(1.3,0.8,z-tz,0,0,0,0) 
    rimDouble4b = semicircle_b(1.3,0.8,z-tz,0,0,0,0)

    rim5a = BEZIER(S1)([[0.15,0.16,z],[0.05,0.6,z]])
    rim5b = BEZIER(S1)([[-0.15,0.16,z],[-0.05,0.6,z]])
    rimDouble5a = BEZIER(S1)([[0.15,0.16,z-tz],[0.05,0.6,z-tz]])
    rimDouble5b = BEZIER(S1)([[-0.15,0.16,z-tz],[-0.05,0.6,z-tz]])

    
    a9 = MAP(BEZIER(S2)([rim1a,rim2a]))(domaininv)
    a10 = MAP(BEZIER(S2)([rim1b,rim2b]))(domain1)
    a11 = MAP(BEZIER(S2)([rim3a,rim4a]))(domaininv)
    a12 = MAP(BEZIER(S2)([rim3b,rim4b]))(domain1)
    a13 = MAP(BEZIER(S2)([rim5a,rim5b]))(domaininv)
    
    a17 = MAP(BEZIER(S2)([rim1a,rimDouble1a]))(domaininv)
    a18 = MAP(BEZIER(S2)([rim2a,rimDouble2a]))(domain1)
    a19 = MAP(BEZIER(S2)([rim3a,rimDouble3a]))(domaininv)
    a20 = MAP(BEZIER(S2)([rim4a,rimDouble4a]))(domain1)
    a21 = MAP(BEZIER(S2)([rim5a,rimDouble5a]))(domaininv)

    a22 = MAP(BEZIER(S2)([rim1b,rimDouble1b]))(domaininv)
    a23 = MAP(BEZIER(S2)([rim2b,rimDouble2b]))(domain1)
    a24 = MAP(BEZIER(S2)([rim3b,rimDouble3b]))(domaininv)
    a25 = MAP(BEZIER(S2)([rim4b,rimDouble4b]))(domain1)
    a26 = MAP(BEZIER(S2)([rim5b,rimDouble5b]))(domaininv)
    
    a27 = MAP(BEZIER(S2)([rimDouble1a,rimDouble2a]))(domaininv)
    a28 = MAP(BEZIER(S2)([rimDouble1b,rimDouble2b]))(domain1)
    a29 = MAP(BEZIER(S2)([rimDouble3a,rimDouble4a]))(domaininv)
    a30 = MAP(BEZIER(S2)([rimDouble3b,rimDouble4b]))(domain1)
    a31 = MAP(BEZIER(S2)([rimDouble5a,rimDouble5b]))(domaininv)
    
    radius = STRUCT([a13,a21,a26,a31])
    a14 = T([1,2])(-0.05)(R([1,2])(PI/2)(radius))
    a15 = R([1,2])(PI)(radius)
    a16 = T([1,2])(0.05)(R([1,2])(3*PI/2)(radius))

    a32 = T([1,2])(-0.05)(R([1,2])(PI/2)(radius))
    a33 = R([1,2])(PI)(radius)
    a34 = T([1,2])(0.05)(R([1,2])(3*PI/2)(radius))
    
    part1 = STRUCT([a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20])
    part2 = STRUCT([a21,a22,a23,a24,a25,a26,a27,a28,a29,a30,a31,a32,a33,a34])
    return STRUCT([part1,part2])



a1 = MAP(BEZIER(S2)([wheel1a,wheel2a]))(domain1)
a2 = MAP(BEZIER(S2)([wheel1b,wheel2b]))(domaininv)
a3 = MAP(BEZIER(S2)([wheel3a,wheel1a]))(domain1)
a4 = MAP(BEZIER(S2)([wheel3b,wheel1b]))(domaininv)
a5 = MAP(BEZIER(S2)([wheel3a,wheel4a]))(domaininv)

a6 = MAP(BEZIER(S2)([wheel3b,wheel4b]))(domain1)
a7 = MAP(BEZIER(S2)([wheel2b,wheel4b]))(domain1)
a8 = MAP(BEZIER(S2)([wheel2a,wheel4a]))(domaininv)

rim1 = rim_star(0,0,0.1)
rim2 = rim_star(1,1,0.1)

wheel = S([1,2,3])([2,2,2])(STRUCT([a1,a2,a3,a4,a5,a6,a7,a8,T([3,1])(0.1)(rim1),rim2]))

skeleton_and_wheels = STRUCT([T([3,1])(-4.6)(T([1,2])(-8)(T([2,1])(-3.3)(wheel))),T([3,1])(2.5)(T([1,2])(-8)(T([2,1])(-3.3)(wheel))),
    T([3,1])(2.5)(T([1,2])(9)(T([2,1])(-3.3)(wheel))),skeleton,T([3,1])(-4.6)(T([1,2])(9)(T([2,1])(-3.3)(wheel)))])



#build the external part of the steering wheel
steer1a = semicircle_a(0.45,0.3,0,0,0,0,0)
steer1b = semicircle_b(0.45,0.3,0,0,0,0,0)

steer2a = semicircle_a(0.5,0.35,0.03,0,0,0,0)
steer2b = semicircle_b(0.5,0.35,0.03,0,0,0,0)

steer3a = semicircle_a(0.5,0.35,0.05,0,0,0,0)
steer3b = semicircle_b(0.5,0.35,0.05,0,0,0,0)

steer4a = semicircle_a(0.45,0.3,0.07,0,0,0,0)
steer4b = semicircle_b(0.45,0.3,0.07,0,0,0,0)


steerUp = MAP(BEZIER(S2)([steer1a,steer2a,steer3a,steer4a]))(domain1)
steerDown = MAP(BEZIER(S2)([steer1b,steer2b,steer3b,steer4b]))(domaininv)
steerZ1 = MAP(BEZIER(S2)([steer1a,steer4a]))(domaininv) 
steerZ2 = MAP(BEZIER(S2)([steer1b,steer4b]))(domain1)
external = COLOR(BLACK)(STRUCT([steerUp,steerDown,steerZ1,steerZ2]))

#build the internal part of the steering wheel
inter1a = semicircle_a(0.15,0.1,0,0,0,0,0) 
inter1b = semicircle_b(0.15,0.1,0,0,0,0,0)



inter1az = semicircle_a(0.15,0.1,0.05,0,0,0,0) 
inter1bz = semicircle_b(0.15,0.1,0.05,0,0,0,0)


inter2a = semicircle_a(0.3,0.2,0,0,0,0,0)
inter2b = semicircle_b(0.3,0.2,0,0,0,0,0)

inter2az = semicircle_a(0.3,0.2,0.045,0,0,0,0)
inter2bz = semicircle_b(0.3,0.2,0.045,0,0,0,0)


inter3a = semicircle_a(0.35,0.25,0.02,0,0,0,0) 
inter3b = semicircle_b(0.35,0.25,0.02,0,0,0,0)


inter4a = semicircle_a(0.35,0.25,0.03,0,0,0,0) 
inter4b = semicircle_b(0.35,0.25,0.03,0,0,0,0)


inter1 = MAP(BEZIER(S2)([inter1a,inter2a]))(domaininv)
inter2 = MAP(BEZIER(S2)([inter1b,inter2b]))(domain1)

inter4 = MAP(BEZIER(S2)([inter1a,inter1az]))(domain1)
inter5 = MAP(BEZIER(S2)([inter2a,inter3a,inter4a,inter2az]))(domain1)
inter6 = MAP(BEZIER(S2)([inter1b,inter1bz]))(domaininv)
inter7 = MAP(BEZIER(S2)([inter2b,inter3b,inter4b,inter2bz]))(domaininv)
inter8 = MAP(BEZIER(S2)([inter1az,inter2az]))(domaininv)

inter9 = MAP(BEZIER(S2)([inter1bz,inter2bz]))(domain1)

inter3 = COLOR(YELLOW)(MAP(BEZIER(S2)([inter1a,inter1b]))(domain1))
inter10 = COLOR(YELLOW)(MAP(BEZIER(S2)([inter1az,inter1bz]))(domain1))


internalpart1 = COLOR([0.5,0.5,0.5])(STRUCT([inter1,inter2,inter4,inter5,inter6,inter7,inter8,inter9]))
internalpart2 = STRUCT([inter3,inter10])
internal = STRUCT([internalpart1,internalpart2])

#build the internal decoration of the steering wheel
domain1D = GRID([30])
r1 = BEZIER(S1)([[0.06,-0.04,0],[0,-0.03,0.35]])
r1_map= MAP(r1)(domain1D)
r11 = BEZIER(S1)([[0.06,0.04,0],[0,0.04,0.35]])
r11_map = MAP(r11)(domain1D)
r1_b = BEZIER(S1)([[0.065,-0.04,0],[0.005,-0.03,0.35]])
r1_bmap = MAP(r1_b)(domain1D)
r12_b = BEZIER(S1)([[0.065,0.04,0],[0.005,0.04,0.35]])
r12_bmap = MAP(r12_b)(domain1D)

s1 = BEZIER(S2)([r1,r11])
part1 = MAP(s1)(domain1)
s2 = BEZIER(S2)([r1_b,r12_b]) 
part2 = MAP(s2)(domaininv)
s3 = BEZIER(S2)([r1,r1_b])
part3 = MAP(s3)(domaininv)
s4 = BEZIER(S2)([r11,r12_b])
part4 = MAP(s4)(domain1)

radius = STRUCT([part1,part2,part3,part4])

tri_radius = COLOR(GRAY)(STRUCT([radius,R([2,3])((2*PI)/3)(radius),R([2,3])((4*PI)/3)(radius)]))

steelingWheel = STRUCT([T([3,1])(0.03)(S([1,2,3])([0.65,0.65,0.65])(R([3,1])(-PI/2)(tri_radius))),
    S([1,2,3])([0.5,0.5,0.5])(T([3,1])(0.1)(internal)),external])

steeling_skeleton_wheels = STRUCT([R([2,3])(PI/8)(T([1,2])(-5)(T([3,1])(2)(R([3,1])(PI/2)(S([1,2,3])([7,7,7])(steelingWheel))))),skeleton_and_wheels])





ControlPoints = [[-12.8,0],[-6,0],[-6,0],[-6,3],[-2,3],[-2,0],[-2,0],[11,0],[11,0],[11,3],
				 [15,3],[15,0],[15,0],[18,1],[19,1.5],[19,2.5],[19,2.5],[18,2.5],[18,2.5],[18,3.5],
				 [18,3.5],[18.5,3.5],[18.5,3.5],[18.5,4]]
lateral_down = NUBSPLINE(3)([0,0,0,0, 1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,17,18,19,20,20,21,21,21,21])(ControlPoints)

ControlPoints2 = [[18.5,4],[17.5,4],[17.5,4],[11,6.5],[11,6.5],[10.8,6.8],[10.8,6.8],[7,7.5],[3,7.5],[3,7.5]
				,[-3,5],[-3,5],[-3.8,5],[-8,4.5],[-9.5,4],[-9.5,4],[-13,3.3],[-13,3.3],[-13,3],[-13,3],
				[-13,1.7],[-13,1.7],[-12.5,1.4],[-12.8,0.9],[-12.8,0.9],[-12.8,0.9],[-12.8,0],[-12.8,0],[-12.8,0],[-12.8,0]]

lateral_up = NUBSPLINE(3)([0,0,0,0,1,2,3,4,5,6,   7,8,9,10,11,12,13,14,15,16,    17,18,19,20,21,22,23,24,25,26,27,27,27,27])(ControlPoints2)
lateralSection = T([2,1])(-4)(T([1,2])(-4)(STRUCT([lateral_down,lateral_up])))



upsec1 = BEZIER(S1)([[0,0,0],[0.4,0,0.5],[4.8,0,0.5],[7,0,0.3]])
upsec2 = BEZIER(S1)([[0,0,0],[-0.5,0,-0.5],[-0.5,0,-8],[0,0,-8]])
upsec3 = BEZIER(S1)([[7,0,0.3],[8.5,0,0.3]])
upsec4 = BEZIER(S1)([[8.5,0,0.3],[10.5,0,0.4]])
upsec5 = BEZIER(S1)([[10.5,0,0.4],[16,0,1],[17,0,0.8]])
upsec6 = BEZIER(S1)([[17,0,0.8],[17,0,0.75],[19,0,0.75],[19,0,0.8]])
upsec7 = BEZIER(S1)([[19,0,0.8],[22,0,1.2]])
upsec8 = BEZIER(S1)([[22,0,1.2],[22.8,0,1.2],[22.8,0,-9.2],[22,0,-9.2],[22,0,-9.2]])
upmap1 = MAP(BEZIER(S2)([upsec1]))(domain2D)
upmap2 = MAP(BEZIER(S2)([upsec2]))(domain2D)
upmap3 = MAP(BEZIER(S2)([upsec3]))(domain2D)
upmap4 = MAP(BEZIER(S2)([upsec4]))(domain2D)
upmap5 = MAP(BEZIER(S2)([upsec5]))(domain2D)
upmap6 = MAP(BEZIER(S2)([upsec6]))(domain2D)
upmap7 = MAP(BEZIER(S2)([upsec7]))(domain2D)
upmap8 = MAP(BEZIER(S2)([upsec8]))(domain2D)

uplateral = STRUCT([upmap1,upmap3,upmap4,upmap5,upmap6,upmap7])
upSection = T([3,1])(4)(T([1,3])(-12)(STRUCT([uplateral,T([3,1])(-8)(R([2,3])(PI)(uplateral)),upmap2,upmap8])))

backsec1 = BEZIER(S1)([[0,0,-0.3],[0,-1,-0.3],[0,-2,-0.3],[0,-2,-0.3],[0,-2,6],[0,-2,6],[0,-1,6],[0,0,6]])
backsec2 = BEZIER(S1)([[0,0,6],[0,0,6]])
backsec3 = BEZIER(S1)([[0,0,6],[0,0.15,5.4]])
backsec4 = BEZIER(S1)([[0,0.15,5.4],[0,0.8,5.2]])
backsec5 = BEZIER(S1)([[0,0.8,5.2],[0,1.2,5],[0,1.2,5],[0,1.2,0.5],[0,1.2,0.5],[0,0.8,0.5],[0,0.15,0.3]])
backsec6 = BEZIER(S1)([[0,0.15,0.3],[0,0,-0.3]])


backmap1 = MAP(BEZIER(S2)([backsec1]))(domain2D)
backmap2 = MAP(BEZIER(S2)([backsec2]))(domain2D)
backmap3 = MAP(BEZIER(S2)([backsec3]))(domain2D)
backmap4 = MAP(BEZIER(S2)([backsec4]))(domain2D)
backmap5 = MAP(BEZIER(S2)([backsec5]))(domain2D)

backmap6 = MAP(BEZIER(S2)([backsec6]))(domain2D)
backSection = T([2,1])(0.5)(T([3,1])(-2.7)(STRUCT([backmap1,backmap2,backmap3,backmap4,backmap5,backmap6])))

skeleton = STRUCT([S([1,2,3])([1.38,1,1])(upSection),lateralSection,S([1,2,3])([1.7,1.7,1.7])(backSection)])


points = [[-13,3.3],[-13,3.3],[-13,3],[-13,3],
                [-13,1.7],[-13,1.7],[-12.5,1.4],[-12.8,0.9],[-12.8,0.9],[-12.8,0.9],[-12.8,0],[-12.8,0],[-12.8,0],[-12.8,0]]


part13D = BEZIER(S1)([[18.5,4],[17.5,4]])

part23D = BEZIER(S1)([[17.5,4,0],[11,6.5,0],[10.8,6.8,0]])

part33D = BEZIER(S1)([[10.8,6.8,0],[7,7.5,0],[3,7.5,0]])
part43D = BEZIER(S1)([[3,7.5,0],[-3,5,0],[-3.8,5,0]])
part53D = BEZIER(S1)([[-3.8,5,0],[-8,4.5,0],[-9.5,4,0],[-9.5,4,0]])
part63D = BEZIER(S1)([[10.8,6.8,0],[10.8,6.8,-8]])
part73D = BEZIER(S1)([[3,7.55,-0.1],[3,7.54,-7.7]])
part83D = BEZIER(S1)([[2.8,7.4,-0.1],[2.8,7.4,-7.7]])


part93D = BEZIER(S1)([[3,7.5,-0.3],[-3,5,-0.3],[-3.8,5,-0.3]])
part103D = BEZIER(S1)([[3,7.5,-7.7],[-3,5,-7.7],[-3.8,5,-7.7]])
part113D = BEZIER(S1)([[3,7.5,-8],[-3,5,-8],[-3.8,5,-8]])

part123D = BEZIER(S1)([[-3.8,5,-0.3],[-3.8,5,-7.7]])
part133D = BEZIER(S1)([[-3.5,5.1,-0.3],[-3.5,5.1,-7.7]])
part143D = BEZIER(S1)([[10.8,6.8,-8],[7,7.5,-8],[3,7.5,-8]])

part153D = BEZIER(S1)([[10.8,6.8,0],[10.8,6.8,-8]])
part163D = BEZIER(S1)([[12,6.3,0],[12,6.3,-8]])

part173D = BEZIER(S1)([[17.5,4,-0.35],[11,6.5,-0.35],[10.8,6.8,-0.35]])

part183D = BEZIER(S1)([[17.5,4,-8],[11,6.5,-8],[10.8,6.8,-8]])

part193D = BEZIER(S1)([[17.5,4,-7.7],[11,6.5,-7.7],[10.8,6.8,-7.7]])

part203D = BEZIER(S1)([[15.6,4.8,0],[15.6,4.8,-8]])
part213D = BEZIER(S1)([[16,4.5,0],[16,4.5,-8]])
part223D = BEZIER(S1)([[-3.8,5,-8],[-8,4.5,-8],[-9.5,4,-8],[-9.5,4,-8]])
part233D = BEZIER(S1)([[-3.8,5.5,-2],[-8,5,-2],[-9.5,4.5,-2],[-9.5,4.5,-2]])
part243D = BEZIER(S1)([[-3.8,5.5,-4],[-8,5,-4],[-9.5,4.5,-4],[-9.5,4.5,-4]])



skel3D3 = COLOR(RED)(MAP(BEZIER(S2)([part73D,part83D]))(domain2D))
skel3D4 = COLOR(RED)(MAP(BEZIER(S2)([part43D,part93D]))(domain2Dinv))
skel3D5 = COLOR(RED)(MAP(BEZIER(S2)([part103D,part113D]))(domain2Dinv))
skel3D6 = COLOR(RED)(MAP(BEZIER(S2)([part123D,part133D]))(domain2Dinv))
skel3D7 = COLOR([0,110,110,0.2])(MAP(BEZIER(S2)([part93D,part103D]))(domain2Dinv))
skel3D8 = COLOR(RED)(MAP(BEZIER(S2)([part33D,part143D]))(domain2Dinv))
skel3D9 = COLOR(RED)(MAP(BEZIER(S2)([part153D,part163D]))(domain2Dinv))

skel3D12 = COLOR(RED)(MAP(BEZIER(S2)([part203D,part213D]))(domain2Dinv))
skel3D13 = COLOR([0,110,110,0.2])(MAP(BEZIER(S2)([part203D,part163D]))(domain2Dinv))
skel3D14 = COLOR(RED)(MAP(BEZIER(S2)([part53D,part243D,part243D,part223D]))(domain2Dinv))
skel3D15 = COLOR(RED)(MAP(BEZIER(S2)([part23D,part193D]))(domain2Dinv))

upSkeleton3D = STRUCT([skel3D3,skel3D4,skel3D5,skel3D6,skel3D7,skel3D8,skel3D9,skel3D12,skel3D13,skel3D14])




do1 = BEZIER(S1)([[0,0,0],[0,1,0],[0,1,0],[0.1,1.1,0]])
do2 = BEZIER(S1)([[15.9,0,0],[15.9,1,0],[15.9,1,0],[15.9,1.1,0]]) 

doorDown = COLOR(RED)(MAP(BEZIER(S2)([do1,do2]))(domain2Dinv))

do5 = BEZIER(S1)([[3,7.5,-0.3],[-3,5,-0.3],[-3.8,5,-0.3]])

do6 = BEZIER(S1)([[3,8,-0.3],[-3,5.5,-0.3],[-3.8,5.5,-0.3]])

do7 = BEZIER(S1)([[3,7.5,-0.3],[12,7.5,-0.3]])
do8 = BEZIER(S1)([[3,8,-0.3],[12,8,-0.3]])

do9 = BEZIER(S1)([[11.7,8,-0.3],[11.7,5,-0.3]])
do10 = BEZIER(S1)([[12,7.5,-0.3],[12,5,-0.3]])

doorup1 = COLOR(RED)(MAP(BEZIER(S2)([do5,do6]))(domain2Dinv))

doorup2 = COLOR(RED)(MAP(BEZIER(S2)([do7,do8]))(domain2D))

doorup3 = COLOR(RED)(MAP(BEZIER(S2)([do9,do10]))(domain2D))

doornot = STRUCT([T([3,1])(-0.3)(T([1,2])(-3.9)(T([2,1])(2.8)(S([1,2,3])([1,2.5,2])(doorDown)))),doorup1,doorup2,doorup3])
door = T([1,2])(-2)(T([2,1])(-5)(S([1,2,3])([0.6,1,1])(doornot)))


final_model = STRUCT([T([3,1])(5)(door),steeling_skeleton_wheels,T([1,2])(-3)(T([3,1])(4)(upSkeleton3D)),T([3,1])(-5)(door)])
VIEW(final_model)




