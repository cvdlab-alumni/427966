
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


domain1 = INTERVALS(1)(60);
domain2 =  PROD1x1([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)
/*************************************************T20 FASCIA SPECCHIATA****************************************************/

/*THE LEGS OF THE TABLE*/
z_leg = 0.85
y_leg = 0.03

curve_leg1 = BEZIER(S1)([[0.3,0,0],[0,0,0],[-0.5,0.9,0],[0.5,1.5,0],[0.8,1.3,0],[1.5,1,0],[1.3,0,0],[1,0,0]])
curve_leg2 = BEZIER(S1)([[0.3,0,z_leg],[0,0,z_leg],[-0.5,0.9,z_leg],[0.5,1.5,z_leg],[0.8,1.3,z_leg],[1.5,1,z_leg],[1.3,0,0.5],[1,0,z_leg]])
curve_leg3 = BEZIER(S1)([[0.2,0+y_leg,0],[0.3,0+y_leg,0],[-0.05,0+y_leg,0],[-0.6,0.9+y_leg,0],[0.5,1.5+y_leg,0],[0.8,1.3+y_leg,0],
	[1.6,0.95+y_leg,0],[1.3,0+y_leg,0],[1,0+y_leg,0]])
curve_leg4 = BEZIER(S1)([[0.2,0+y_leg,z_leg],[0.3,0+y_leg,z_leg],[-0.05,0+y_leg,z_leg],[-0.6,0.9+y_leg,z_leg],[0.5,1.5+y_leg,z_leg],[0.8,1.3+y_leg,z_leg],
	[1.6,0.95+y_leg,z_leg],[1.3,0+y_leg,z_leg],[1,0+y_leg,z_leg]])

map1_leg = MAP(BEZIER(S2)([curve_leg1,curve_leg2]))(domain2)
map2_leg = MAP(BEZIER(S2)([curve_leg3,curve_leg4]))(domain2)
map3_leg = MAP(BEZIER(S2)([curve_leg1,curve_leg3]))(domain2)
map4_leg = MAP(BEZIER(S2)([curve_leg2,curve_leg4]))(domain2)
leg1 = COLOR([64/255,64/255,64/255])(STRUCT([map1_leg,map2_leg,map3_leg,map4_leg]))
leg2 = T([1])([0.7])(T([2])([0.5])(R([1,2])([PI])(leg1)))
legs = STRUCT([leg1,leg2])

/*THE UP PART OF THE TABLE*/
curve_table1a = semicircle_a(2.3,1.5,0,0,0,0,0)
curve_table1b = semicircle_b(2.3,1.5,0,0,0,0,0)
curve_table2a = semicircle_a(2.3,1.5,0.03,0,0,0,0)
curve_table2b = semicircle_b(2.3,1.5,0.03,0,0,0,0)

curve_table3a = semicircle_a(2.8,1.9,0,0,0,0,0)
curve_table3b = semicircle_b(2.8,1.9,0,0,0,0,0)
curve_table4a = semicircle_a(2.8,1.9,0.03,0,0,0,0)
curve_table4b = semicircle_b(2.8,1.9,0.03,0,0,0,0)

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

table_traslation = function(object){ return T([2])([0.25])(T([1])([0.3])(T([3])([z_leg])(object))) }

table1_up = COLOR([1,1,1,0.7])(table_traslation(STRUCT([map1_tableup,map2_tableup,map3_tableup,map4_tableup])))
table2_up = COLOR([159/255,182/255,205/255,1])(table_traslation(STRUCT([map5_tableup,map6_tableup,map7_tableup,map8_tableup,map9_tableup,map10_tableup])))
table_up = STRUCT([table1_up,table2_up])

/*THE FINAL MODEL OF T20 FASCIA SPECCHIATA*/
t20_fascia_specchiata = STRUCT([table_up,legs])
