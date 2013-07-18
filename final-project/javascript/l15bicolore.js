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


function repeatTraslation(object,ax,t,n){
stripes = object
for (var i = 1; i < n; i++) {
stripes = STRUCT([stripes,T([ax])([t*i])(object)])

};
return stripes
}

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



COLOR_WOOD = [255/255,165/255,79/255];
COLOR_BLACK = [51/255,51/255,51/255];
domain1 = INTERVALS(1)(32);
domain2 =  PROD1x1([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)


/*****************************************************L15 BICOLORE***************************************************/

/****************************************************THE FRONT PART*****************************************************/

/*THE CURVES OF THE FRONT PART*/
curve1_front = BEZIER(S1)([[0,0,0],[0,2.5,0]])
curve2_front = BEZIER(S1)([[0,2.5,0],[0.4,2.5,0],[0.4,2.8,0],[0,2.8,0]])
curve3_front = BEZIER(S1)([[0,2.8,0],[0,2.9,0]])
curve4_front = BEZIER(S1)([[6,0,0],[6,2.5,0]])
curve5_front = BEZIER(S1)([[6,2.5,0],[5.6,2.5,0],[5.6,2.8,0],[6,2.8,0]])
curve6_front = BEZIER(S1)([[6,2.8,0],[6,2.9,0]])
curve7_front = BEZIER(S1)([[0,0,0.2],[0,2.5,0.2]])
curve8_front = BEZIER(S1)([[0,2.5,0.2],[0.4,2.5,0.2],[0.4,2.8,0.2],[0,2.8,0.2]])
curve9_front = BEZIER(S1)([[0,2.8,0.2],[0,2.9,0.2]])
curve10_front = BEZIER(S1)([[6,0,0.2],[6,2.5,0.2]])
curve11_front = BEZIER(S1)([[6,2.5,0.2],[5.6,2.5,0.2],[5.6,2.8,0.2],[6,2.8,0.2]])
curve12_front = BEZIER(S1)([[6,2.8,0.2],[6,2.9,0.2]])

/*THE MAPS OF THE FRONT PART*/
map1_front = MAP(BEZIER(S2)([curve1_front,curve4_front]))(domain2)
map2_front = MAP(BEZIER(S2)([curve2_front,curve5_front]))(domain2)
map3_front = MAP(BEZIER(S2)([curve3_front,curve6_front]))(domain2)
map4_front = MAP(BEZIER(S2)([curve1_front,curve7_front]))(domain2)
map5_front = MAP(BEZIER(S2)([curve2_front,curve8_front]))(domain2)
map6_front = MAP(BEZIER(S2)([curve3_front,curve9_front]))(domain2)
map7_front = MAP(BEZIER(S2)([curve4_front,curve10_front]))(domain2)
map8_front = MAP(BEZIER(S2)([curve5_front,curve11_front]))(domain2)
map9_front = MAP(BEZIER(S2)([curve6_front,curve12_front]))(domain2)
map10_front = MAP(BEZIER(S2)([curve7_front,curve10_front]))(domain2)
map11_front = MAP(BEZIER(S2)([curve8_front,curve11_front]))(domain2)
map12_front = MAP(BEZIER(S2)([curve9_front,curve12_front]))(domain2)
 
/*THE MODEL OF THE FRONT PART*/
front = COLOR(COLOR_BLACK)(T([3])([-0.2])(STRUCT([map1_front,map2_front,map3_front,map4_front,map5_front,map6_front,
  map7_front,map8_front,map9_front,map10_front,map11_front,map12_front])))

/* THE CURVES OF THE UP PART OF THE FRONT*/
curve1_frontup = BEZIER(S1)([[0,0.35,0],[-0.8,0.35,0],[-0.8,-0.35,0],[0,-0.35,0]])
curve2_frontup = BEZIER(S1)([[8,0.35,0],[8.8,0.35,0],[8.8,-0.35,0],[8,-0.35,0]])
curve3_frontup = BEZIER(S1)([[0,0.35,-0.2],[-0.8,0.35,-0.2],[-0.8,-0.35,-0.2],[0,-0.35,-0.2]])
curve4_frontup = BEZIER(S1)([[8,0.35,-0.2],[8.8,0.35,-0.2],[8.8,-0.35,-0.2],[8,-0.35,-0.2]])
curve5_frontup = BEZIER(S1)([[0,0.35,0],[8,0.35,0]])
curve6_frontup = BEZIER(S1)([[0,-0.35,0],[8,-0.35,0]])
curve7_frontup = BEZIER(S1)([[0,0.35,-0.2],[8,0.35,-0.2]])
curve8_frontup = BEZIER(S1)([[0,-0.35,-0.2],[8,-0.35,-0.2]])
curve9_frontup = BEZIER(S1)([[0,0.3,0.05],[-0.7,0.3,0.05],[-0.7,-0.3,0.05],[0,-0.3,0.05]])
curve10_frontup = BEZIER(S1)([[8,0.3,0.05],[8.7,0.3,0.05],[8.7,-0.3,0.05],[8,-0.3,0.05]])
curve11_frontup = BEZIER(S1)([[0,0.3,-0.25],[-0.7,0.3,-0.25],[-0.7,-0.3,-0.25],[0,-0.3,-0.25]])
curve12_frontup = BEZIER(S1)([[8,0.3,-0.25],[8.7,0.3,-0.25],[8.7,-0.3,-0.25],[8,-0.3,-0.25]])
curve13_frontup = BEZIER(S1)([[0,0.3,0.05],[8,0.3,0.05]])
curve14_frontup = BEZIER(S1)([[0,-0.3,0.05],[8,-0.3,0.05]])
curve15_frontup = BEZIER(S1)([[0,0.3,-0.25],[8,0.3,-0.25]])
curve16_frontup = BEZIER(S1)([[0,-0.3,-0.25],[8,-0.3,-0.25]])

/*THE MAPS OF THE UP PART OF THE FRONT*/
map1_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve1_frontup,curve3_frontup]))(domain2))
map2_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve2_frontup,curve4_frontup]))(domain2))
map3_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve5_frontup,curve6_frontup]))(domain2))
map4_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve5_frontup,curve7_frontup]))(domain2))
map5_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve6_frontup,curve8_frontup]))(domain2))
map6_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve7_frontup,curve8_frontup]))(domain2))
map7_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve1_frontup,curve2_frontup]))(domain2))
map8_frontup = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve3_frontup,curve4_frontup]))(domain2))
map9_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve9_frontup,curve11_frontup]))(domain2))
map10_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve10_frontup,curve12_frontup]))(domain2))
map11_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve9_frontup,curve10_frontup]))(domain2))
map12_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve11_frontup,curve12_frontup]))(domain2))
map13_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve13_frontup,curve15_frontup]))(domain2))
map14_frontup = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve14_frontup,curve16_frontup]))(domain2))

/*THE MODEL OF THE UP PART OF THE FRONT*/
frontup = STRUCT([map1_frontup,map2_frontup,map3_frontup,map4_frontup,map5_frontup,map6_frontup,
  map7_frontup,map8_frontup,map9_frontup,map10_frontup,map11_frontup,map12_frontup,map13_frontup,map14_frontup])

/**************************************************THE MATTRESS***************************************************/

/*THE CURVES OF THE MATTRESS*/

curve1_mattress = BEZIER(S1)([[0.3,0,0],[0,0,0],[0,8,0],[0.3,8,0]])
curve2_mattress = BEZIER(S1)([[5.7,0,0],[6,0,0],[6,8,0],[5.7,8,0]])
curve3_mattress = BEZIER(S1)([[0.3,0,0.4],[0,0,0.4],[0,8,0.4],[0.3,8,0.4]])
curve4_mattress = BEZIER(S1)([[5.7,0,0.4],[6,0,0.4],[6,8,0.4],[5.7,8,0.4]])
curve5_mattress = BEZIER(S1)([[0.3,0,0],[5.7,0,0]])
curve6_mattress = BEZIER(S1)([[0.3,0,0.4],[5.7,0,0.4]])
curve7_mattress = BEZIER(S1)([[0.3,8,0],[5.7,8,0]])
curve8_mattress = BEZIER(S1)([[0.3,8,0.4],[5.7,8,0.4]])
curve9_mattress = BEZIER(S1)([[3,0,-0.5],[3,8,-0.5]])
curve10_mattress = BEZIER(S1)([[0.3,8,0],[1.5,8,-0.33],[4.5,8,-0.33],[5.7,8,0]])

/*THE MAPS OF THE MATTRESS*/
map1_mattress = MAP(BEZIER(S2)([curve1_mattress,curve9_mattress,curve2_mattress]))(domain2)
map2_mattress = MAP(BEZIER(S2)([curve3_mattress,curve4_mattress]))(domain2)
map3_mattress = MAP(BEZIER(S2)([curve1_mattress,curve3_mattress]))(domain2)
map4_mattress = MAP(BEZIER(S2)([curve2_mattress,curve4_mattress]))(domain2)
map5_mattress = MAP(BEZIER(S2)([curve5_mattress,curve6_mattress]))(domain2)
map6_mattress = MAP(BEZIER(S2)([curve7_mattress,curve8_mattress]))(domain2)
map7_mattress = MAP(BEZIER(S2)([curve7_mattress,curve10_mattress]))(domain2)

/*THE MODEL OF THE MATTRESS*/
mattress = COLOR([255/255,255/255,255/255])(T([1])([1])(T([2])([-1])(R([2,3])(PI/2)(STRUCT([map1_mattress,map2_mattress,map3_mattress,
  map4_mattress,map5_mattress,map6_mattress,map7_mattress])))))

/*************************************************THE GRID***************************************************/

curve1_grid = BEZIER(S1)([[0,0,0],[0,8,0]])
curve2_grid = BEZIER(S1)([[1,0,0],[1,8,0]])
curve1_grid = BEZIER(S1)([[0,0,0.2],[0,8,0.2]])
curve2_grid = BEZIER(S1)([[1,0,0.2],[1,8,0.2]])

grid_horizontal = CUBOID([5.6,0.05,0.01])
grid_horizontals = repeatTraslation(grid_horizontal,2,0.1,79)
grid_vertical = CUBOID([0.05,7.8,0.01])
grid_verticals = repeatTraslation(grid_vertical,1,0.1,57)

grid = T([1])([1.2])(T([2])([-1.4])(R([2,3])(PI/2)(STRUCT([grid_horizontals,grid_verticals]))))

border1 = T([1])([1.1])(T([2])([-1.4])(R([2,3])(PI/2)(CUBOID([5.8,0.2,0.2]))))
border2 = T([3])([7.8])(T([1])([1.05])(T([2])([-1.4])(R([2,3])(PI/2)(CUBOID([5.8,0.2,0.2])))))
border3 = T([1])([1.2])(T([2])([-1.6])(R([1,3])(-PI/2)(CUBOID([8,0.2,0.2]))))
border4 = T([1])([7])(T([2])([-1.6])(R([1,3])(-PI/2)(CUBOID([8,0.2,0.2]))))

grid_structure = COLOR(COLOR_BLACK)(T([1])([-0.03])(STRUCT([grid,border1,border2,border3,border4])))

/**************************************************************THE LEGS********************************************/

/*THE CURVES OF THE LEG*/
curve1_leg = BEZIER(S1)([[0,0.35,0],[-0.8,0.35,0],[-0.8,-0.35,0],[0,-0.35,0]])
curve2_leg = BEZIER(S1)([[2,0.35,0],[2,-0.35,0]])
curve3_leg = BEZIER(S1)([[0,0.35,-0.2],[-0.8,0.35,-0.2],[-0.8,-0.35,-0.2],[0,-0.35,-0.2]])
curve4_leg = BEZIER(S1)([[2,0.35,-0.2],[2,-0.35,-0.2]])
curve5_leg = BEZIER(S1)([[0,0.35,0],[2,0.35,0]])
curve6_leg = BEZIER(S1)([[0,-0.35,0],[2,-0.35,0]])
curve7_leg = BEZIER(S1)([[0,0.35,-0.2],[2,0.35,-0.2]])
curve8_leg = BEZIER(S1)([[0,-0.35,-0.2],[2,-0.35,-0.2]])
curve9_leg = BEZIER(S1)([[0,0.3,0.05],[-0.7,0.3,0.05],[-0.7,-0.3,0.05],[0,-0.3,0.05]])
curve10_leg = BEZIER(S1)([[2,0.3,0.05],[2,-0.3,0.05]])
curve11_leg = BEZIER(S1)([[0,0.3,-0.25],[-0.7,0.3,-0.25],[-0.7,-0.3,-0.25],[0,-0.3,-0.25]])
curve12_leg = BEZIER(S1)([[2,0.3,-0.25],[2,-0.3,-0.25]])
curve13_leg = BEZIER(S1)([[0,0.3,0.05],[2,0.3,0.05]])
curve14_leg = BEZIER(S1)([[0,-0.3,0.05],[2,-0.3,0.05]])
curve15_leg = BEZIER(S1)([[0,0.3,-0.25],[2,0.3,-0.25]])
curve16_leg = BEZIER(S1)([[0,-0.3,-0.25],[2,-0.3,-0.25]])

/*THE MAPS OF THE LEG*/
map1_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve1_leg,curve3_leg]))(domain2))
map2_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve2_leg,curve4_leg]))(domain2))
map3_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve5_leg,curve6_leg]))(domain2))
map4_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve5_leg,curve7_leg]))(domain2))
map5_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve6_leg,curve8_leg]))(domain2))
map6_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve7_leg,curve8_leg]))(domain2))
map7_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve1_leg,curve2_leg]))(domain2))
map8_leg = COLOR(COLOR_BLACK)(MAP(BEZIER(S2)([curve3_leg,curve4_leg]))(domain2))
map9_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve9_leg,curve11_leg]))(domain2))
map10_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve10_leg,curve12_leg]))(domain2))
map11_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve9_leg,curve10_leg]))(domain2))
map12_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve11_leg,curve12_leg]))(domain2))
map13_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve13_leg,curve15_leg]))(domain2))
map14_leg = COLOR(COLOR_WOOD)(MAP(BEZIER(S2)([curve14_leg,curve16_leg]))(domain2))

/* THE MODEL OF THE LEGS*/
leg = S([1,2,3])([0.7,0.7,0.7])(STRUCT([map1_leg,map2_leg,map3_leg,map4_leg,map5_leg,map6_leg,
  map7_leg,map8_leg,map9_leg,map10_leg,map11_leg,map12_leg,map13_leg,map14_leg]))

legsx = T([1])([0.85])(T([2])([-1.3])(T([3])([8.15])(R([1,3])(PI/4)(R([1,2])(-PI/2)(leg)))))
legdx = T([1])([7])(T([2])([-1.3])(T([3])([8.25])(R([1,3])(-PI/4)(R([1,2])(-PI/2)(leg)))))

/*THE MODEL OF L15 BICOLORE*/
L15BICOLORE_model = STRUCT([T([2])([-3.05])(T([1])([1])(front)),frontup,mattress,grid_structure,legsx,legdx])
