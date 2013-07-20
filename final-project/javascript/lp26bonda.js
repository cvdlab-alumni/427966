

//Utility functions

//T(dims)(values)(object)

T = function (dims) {
	dims = dims.map(function(dim){
		return dim - 1;
	});
    return function (values) {
      return function (object) {
       return object.clone().translate(dims, values);
      };
    };
  }

//R
R = function (dims) {
	dims = dims.map(function(dim){
		return dim - 1;
	});
    return function (angle) {
      return function (object) {
        return object.clone().rotate(dims, angle);
      };
    };
  }

//S
S = function (dims) {
	dims = dims.map(function(dim){
		return dim - 1;
	});
    return function (values) {
      return function (object) {
        return object.clone().scale(dims, values);
      };
    };
  }


S3=S2
S2=S1
S1=S0

//Funzioni da pyplasm a Plasm.js
VIEW = DRAW



semicircle_a = function(x1,y1,z,tx,ty,tz1,tz2){
  semix = x1/2
  semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]])
  return semia
}

semicircle_b = function(x1,y1,z,tx,ty,tz1,tz2){
  semix = x1/2
  semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]])
  return semib
}

var SEMISPHERE = function (r) {
  var domain = DOMAIN([[0, PI], [0, PI]])([50,50]);
  var mapping = function (v) {
    var a = v[0];
    var b = v[1];
    return [r*SIN(a)*COS(b), r/2*SIN(a)*SIN(b), r*COS(a)];
  };
  var model = MAP(mapping)(domain);
  return model;
};


color_green = [34/255,139/255,34/255]
domain1 = INTERVALS(1)(32);
domain2 =  PROD1x1([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)

/***************************************************LP26B ONDA*****************************************************/

/*THE LAMP STRUCTURE*/

/*THE CURVES OF THE STRUCTURE*/
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


/*THE MAPS OF THE STRUCTURE*/
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

/*THE MODEL OF THE STRUCTURE*/
lamp_structure = COLOR([46/255,139/255,87/255])(S([1,2,3])([0.8,1,1.2])(STRUCT([map1_lamp,map2_lamp,map3_lamp,map4_lamp,map5_lamp,map6_lamp,
  map7_lamp,map8_lamp,map9_lamp,map10_lamp,map11_lamp,map12_lamp])))

/*****************************************************THE BULB********************************************/

/*THE CURVES OF THE BULB*/
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

/*THE MAPS OF THE BULB*/
map1_light = COLOR([255/255,255/255,0/255])(MAP(BEZIER(S2)([curve1a_light,curve1b_light]))(domaininv))
map2_light = COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve2a_light,curve2b_light]))(domain2))
map3_light = COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve1a_light,curve2a_light]))(domain2))
map4_light = COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve1b_light,curve2b_light]))(domain2))
map5_light =  COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve3a_light,curve3b_light]))(domain2))
map6_light =  COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve3a_light,curve4a_light,curve5a_light]))(domain2))
map7_light =  COLOR([61/255,61/255,61/255])(MAP(BEZIER(S2)([curve3b_light,curve4b_light,curve5b_light]))(domain2))
map8_light = MAP(BEZIER(S2)([curve5a_light,curve5b_light]))(domain2)
map9_light = MAP(BEZIER(S2)([curve5a_light,curve6a_light]))(domain2)
map10_light = MAP(BEZIER(S2)([curve5b_light,curve6b_light]))(domain2)
map11_light = MAP(BEZIER(S2)([curve6a_light,curve6b_light]))(domain2)
map12_light =  COLOR([84/255,84/255,84/255])(MAP(BEZIER(S2)([curve7a_light,curve8a_light]))(domain2))
map13_light =  COLOR([84/255,84/255,84/255])(MAP(BEZIER(S2)([curve7b_light,curve8b_light]))(domain2))
map14_light = COLOR([84/255,84/255,84/255])(MAP(BEZIER(S2)([curve8a_light,curve8b_light]))(domain2))

/*THE MODEL OF THE BULB*/
light = T([1])([1.4])(T([2])([1.35])(T([3])([-0.85])(R([1,2])(-PI/3*2.3/3)(R([1,3])(PI/2)(STRUCT([map1_light,map2_light,map3_light,map4_light,
  map5_light,map6_light,map7_light,map8_light,map9_light,map10_light,map11_light,map12_light,map13_light,map14_light]))))))

/*THE GLASS*/
curve1a_glass = semicircle_a(1.2,0.85,0.1,0,0,0,0)
curve1b_glass = semicircle_b(1.2,0.85,0.1,0,0,0,0)
curve2a_glass = semicircle_a(0,0,0.3,0,0,0,0)
curve2b_glass = semicircle_b(0,0,0.3,0,0,0,0)
glass_light = COLOR([255/255,255/255,255/255,0.6])(T([1])([1.5])(T([2])([1.25])(T([3])([-0.83])(R([1,2])(PI/3*2.2/3)(SEMISPHERE(0.64))))));

/*THE STUDS*/
stud = SEMISPHERE(0.1)
studs = T([3])([-0.92])(STRUCT([T([1])([-0.85])(stud),T([1])([3.9])(stud)]))

/*********************************************************THE LP26B ONDA MODEL**************************************************/
lp26bonda = STRUCT([light,lamp_structure,glass_light,studs])






