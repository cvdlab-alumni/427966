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



S3=S2
S2=S1
S1=S0


VIEW = DRAW
NN = REPLICA


semicircle_a = function(x1,y1,z,tx,ty,tz1,tz2){
    semix = x1/2;
    semia = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,ty+y1,z+tz2],[tx-semix,ty+y1,z+tz2],[tx-semix,ty,z+tz1]]);
    return semia;
}
semicircle_b = function(x1,y1,z,tx,ty,tz1,tz2){
    semix = x1/2;
    semib = BEZIER(S1)([[tx+semix,ty,z+tz1],[tx+semix,-y1+ty,z+tz2],[tx-semix,-y1+ty,z+tz2],[tx-semix,ty,z+tz1]]);
    return semib;
}


domain1 = INTERVALS(1)(32);
domain2 =  PROD1x1([domain1,domain1])
domaininv = MAP([S2,S1])(domain2)


/**********************************************THE BOTTLE**********************************************/

/*THE BODY OF THE BOTTLE*/
bottlebody0 = BEZIER(S1)([[0,1.2,0],[0,1.2,1.5],[0,3.8,1.5],[0,3.8,-1.5],[0,1.2,-1.5],[0,1.2,0]]);
bottlebody1 = BEZIER(S1)([[1,0,0],[1,0,4],[1,7,4],[1,7,-4],[1,0,-4],[1,0,0]]);
bottlebody2 = BEZIER(S1)([[2.5,-0.3,0],[2.5,-0.3,5],[2.5,7.7,5],[2.5,7.7,-5],[2.5,-0.3,-5],[2.5,-0.3,0]]);
bottlebody3 = BEZIER(S1)([[4,0,0],[4,0,4],[4,7,4],[4,7,-4],[4,0,-4],[4,0,0]]);
bottlebody4 = BEZIER(S1)([[5,0.3,0],[5,0.3,3.5],[5,6.3,3.5],[5,6.3,-3.5],[5,0.3,-3.5],[5,0.3,0]]);
bottlebody5 = BEZIER(S1)([[7,0.3,0],[7,0.3,3.5],[7,6.3,3.5],[7,6.3,-3.5],[7,0.3,-3.5],[7,0.3,0]]);
bottlebody6 = BEZIER(S1)([[8.5,-0.3,0],[8.5,-0.3,5],[8.5,7.7,5],[8.5,7.7,-5],[8.5,-0.3,-5],[8.5,-0.3,0]]);
bottlebody7 = BEZIER(S1)([[10,0,0],[10,0,4],[10,7,4],[10,7,-4],[10,0,-4],[10,0,0]]);
bottlebody8 = BEZIER(S1)([[11,0,0],[11,0,4],[11,7,4],[11,7,-4],[11,0,-4],[11,0,0]]);
bottlebody9a = BEZIER(S1)([[11,2.25,-2.25],[11,-0.65,-2.25],[11,-0.65,2.25],[11,2.25,2.25]])
bottlebody9b = BEZIER(S1)([[11,2.25,-2.25],[11,5.05,-2.25],[11,5.05,2.25],[11,2.25,2.25]])

/*THE BOTTLE CAP*/
capneck1 = BEZIER(S1)([[-1,1.2,0],[-1,1.2,1.5],[-1,3.8,1.5],[-1,3.8,-1.5],[-1,1.2,-1.5],[-1,1.2,0]]);
capneck2 = BEZIER(S1)([[-1.5,1.2,0],[-1.5,1.2,1.5],[-1.5,3.8,1.5],[-1.5,3.8,-1.5],[-1.5,1.2,-1.5],[-1.5,1.2,0]]);

cap1a = BEZIER(S1)([[-1.5,2,1],[-1.5,3.2,1],[-1.5,3.2,-1],[-1.5,2,-1]]);
cap1b = BEZIER(S1)([[-1.5,2,1],[-1.5,0.8,1],[-1.5,0.8,-1],[-1.5,2,-1]]);

cap2a = BEZIER(S1)([[-2.2,2,1],[-2.2,3.2,1],[-2.2,3.2,-1],[-2.2,2,-1]]);
cap2b = BEZIER(S1)([[-2.2,2,1],[-2.2,0.8,1],[-2.2,0.8,-1],[-2.2,2,-1]]);

capmap1 = COLOR([2,2,2,1])(MAP(BEZIER(S2)([cap1a,cap2a]))(domain2))
capmap2 = COLOR([2,2,2,1])(MAP(BEZIER(S2)([cap1b,cap2b]))(domaininv))
capmap3 = COLOR([0.5,0.5,0.5,1])(MAP(BEZIER(S2)([cap1a,cap1b]))(domaininv))

cap = STRUCT([capmap1,capmap2,capmap3])

/*THE BOTTLE SURFACES*/
st = BEZIER(S2)([capneck2,capneck1]);
s0 = BEZIER(S2)([capneck1,bottlebody0,bottlebody1,bottlebody2,bottlebody3,bottlebody4]);
s1 = BEZIER(S2)([bottlebody4,bottlebody5]);
s2 = BEZIER(S2)([bottlebody5,bottlebody6,bottlebody7]);
s3 = BEZIER(S2)([bottlebody7,bottlebody8]);
s4 = BEZIER(S2)([bottlebody9a,bottlebody9b])

surft = MAP(st)(domain2);
surf0 = COLOR([0.5,50,0.5,0.9])(MAP(s0)(domain2));
surf1 = COLOR([1,0,0,200])(MAP(s1)(domaininv));
surf2 = COLOR([0.5,50,0.5,0.9])(MAP(s2)(domain2));
surf3 = COLOR([0.5,50,0.5,0.9])(MAP(s3)(domain2));
surf4 = COLOR([0,200,0,1])(MAP(s4)(domain2))

bottlebody = STRUCT([surft,surf0,surf1,surf2,surf3,surf4])


/**********************************************THE LETTERS OF THE BOTTLE BRAND**********************************************/

/*THE LETTER 'E'*/
e00 = BEZIER(S1)([[0,-0.95,-0.75],[0,-0.95,-0.5],[0,-0.45,-0.5],[0,-0.45,-0.75]]);
e01 = BEZIER(S1)([[0,-1,-0.75],[0,-1,-0.45],[0,-0.4,-0.45],[0,-0.4,-0.75]]);
e10= BEZIER(S1)([[0,-0.7,-0.55],[0,-0.7,-0.75]])
e11= BEZIER(S1)([[0,-0.65,-0.55],[0,-0.65,-0.75]])
e0 = BEZIER(S2)([e00,e01])
e1 = BEZIER(S2)([e10,e11])
e0Map = MAP(e0)(domain2)
e1Map = MAP(e1)(domain2)

E_letter = STRUCT([e0Map,e1Map])  

/*THE LETTER 'L'*/
l00 = BEZIER(S1)([[0,0,0],[0,-0.8,-0.08],[0,-1,0.25]]);
l01 = BEZIER(S1)([[0,0,0.05],[0,-0.8,0.042],[0,-1,0.3]]);
l10 = BEZIER(S1)([[0,-1,0.25],[0,-1.1,0.3],[0,-1.1,-0.5],[0,-1,-0.5]]);
l11 = BEZIER(S1)([[0,-0.95,0.25],[0,-1.05,0.3],[0,-1.05,-0.5],[0,-0.95,-0.5]]);
l0 = BEZIER(S2)([l00,l01])
l1 = BEZIER(S2)([l10,l11])
l0Map = MAP(l0)(domain2)
l1Map = MAP(l1)(domain2)

L_letter = STRUCT([l0Map,l1Map])

/*THE LETTER 'T'*/
t00 = BEZIER(S1)([[0,0,-1],[0,-1,-1],[0,-0.95,-0.95],[0,-0.95,-1.4]]);
t01 = BEZIER(S1)([[0,0,-0.95],[0,-1,-0.95],[0,-1.05,-0.9],[0,-1,-1.4]]);
t10 = BEZIER(S1)([[0,-0.3,-1.2],[0,-0.35,-1.2],[0,-0.35,-0.8],[0,-0.3,-0.8]])
t11 = BEZIER(S1)([[0,-0.25,-1.2],[0,-0.3,-1.2],[0,-0.3,-0.8],[0,-0.25,-0.8]])
t0 = BEZIER(S2)([t00,t01])
t1 = BEZIER(S2)([t10,t11])
t0Map = MAP(t0)(domain2)
t1Map = MAP(t1)(domain2)

T_letter = T([1])([0.1])(STRUCT([t0Map,t1Map]))

/*THE BRAND 'LETE'*/
lete = R([3,2])(-PI/2)(STRUCT([L_letter,T([1])([0.1])(E_letter),T_letter,T([3])([-1])(E_letter)]))
lete1 = R([2,3])(PI)(R([1,3])(PI/2)(lete))
lete2 = T([2])([1.5])(T([1])([5.5])(T([3])([1.9])(lete1)))

brand = COLOR([255,255,255,200])(lete2)

/*THE FINAL BOTTLE MODEL*/
bottle_model = STRUCT([bottlebody,brand])

/****************************************************THE BUBBLE*************************************************************************/
/* THE BODY OF THE BUBBLE*/
bubble1a = semicircle_a(2,2.2,0,0,0,0,0)
bubble2a = semicircle_a(2,2.4,0.5,0,0,0,0)
bubble3a = semicircle_a(2,2.2,1,0,0,0,0)

bubble1b = semicircle_b(2,1,0,0,0,0,0)
bubble2b = semicircle_b(2,1.1,0.5,0,0,0,0)
bubble3b = semicircle_b(2,1,1,0,0,0,0)

bubble4 = semicircle_b(1.2,0.6,0,0,0,0,0)
bubble5 = semicircle_b(1.2,0.7,0.5,0,0,0,0)

bubble6 = semicircle_b(1.2,0.4,0,0,0,0,0)
bubble7 = semicircle_b(1.2,0.4,0.5,0,0,0,0)

bubble_map1 = MAP(BEZIER(S2)([bubble1a,bubble2a,bubble3a]))(domain2)
bubble_map2 = MAP(BEZIER(S2)([bubble1b,bubble4]))(domain2)
bubble_map3 = MAP(BEZIER(S2)([bubble1a,bubble6]))(domain2)
bubble_map4 = MAP(BEZIER(S2)([bubble3a,bubble3b]))(domain2)

bubble_map6 = MAP(BEZIER(S2)([bubble4,bubble5]))(domain2)
bubble_map7 = MAP(BEZIER(S2)([bubble1b,bubble2b,bubble3b]))(domain2)
bubble_map8 = MAP(BEZIER(S2)([bubble6,bubble7]))(domain2)
bubble_map9 = MAP(BEZIER(S2)([bubble7,bubble5]))(domain2)

bodybubble1 = COLOR([0,1,55,1])(STRUCT([bubble_map1,bubble_map2,bubble_map3,bubble_map4,bubble_map7]))
bodybubble2 = COLOR([1,1,1,1])(STRUCT([bubble_map6,bubble_map8]))
bodybubble3 = COLOR([0,0,0,1])(STRUCT([bubble_map9]))
bodybubble = STRUCT([bodybubble1,bodybubble2,bodybubble3])

/* THE EYES OF THE BUBBLE*/
eye1a = semicircle_a(0.4,0.5,0,0,0,0,0)
eye1b = semicircle_b(0.4,0.5,0,0,0,0,0)
eye = MAP(BEZIER(S2)([eye1a,eye1b]))(domain2)

eye1 = R([2,1])(PI/16)(T([3])([-0.05])(T([2])([0.8])(T([1])([0.5])(eye))))
eye2 = R([2,1])(-PI/16)(T([3])([-0.05])(T([2])([0.8])(T([1])([-0.5])(eye))))
eyes = COLOR([255,255,255])(STRUCT([eye1,eye2]))

/* THE RETINAS OF THE BUBBLE*/
retina1a = semicircle_a(0.2,0.25,0,0,0,0,0)
retina1b = semicircle_b(0.2,0.25,0,0,0,0,0)
retina = MAP(BEZIER(S2)([retina1a,retina1b]))(domain2)

retina1 = R([2,1])(PI/16)(T([3])([-0.06])(T([2])([0.8])(T([1])([0.45])(retina))))
retina2 = R([2,1])(-PI/16)(T([3])([-0.06])(T([2])([0.8])(T([1])([-0.45])(retina))))
retinas = COLOR([0,0,0])(STRUCT([retina1,retina2]))

/* THE HANDS OF THE BUBBLE*/
hand1 = semicircle_a(0.15,0.3,0,0,0,0,0)
hand1z = semicircle_a(0.15,0.3,0.2,0,0,0,0)

hand2 = semicircle_a(0.1,0.4,0,0.17,0,0,0)
hand2z = semicircle_a(0.1,0.4,0.2,0.17,0,0,0)

hand3 = semicircle_a(0.1,0.45,0,0.3,0,0,0)
hand3z = semicircle_a(0.1,0.45,0.2,0.3,0,0,0)

hand4 = semicircle_a(0.07,0.25,0,0.45,0,0,0)
hand4z = semicircle_a(0.07,0.25,0.2,0.45,0,0,0)

hand5 = semicircle_a(0.55,0,0,0.2,0,0,0)
hand5z = semicircle_a(0.55,0,0.2,0.2,0,0,0)

hand6 = semicircle_b(0.56,0.7,0,0.2,0,0,0)
hand6z = semicircle_b(0.56,0.7,0.2,0.2,0,0,0)

m1 = MAP(BEZIER(S2)([hand6,hand5]))(domain2)
m2 = MAP(BEZIER(S2)([hand6,hand1]))(domain2)
m3 = MAP(BEZIER(S2)([hand6,hand2]))(domain2)
m4 = MAP(BEZIER(S2)([hand6,hand3]))(domain2)
m5 = MAP(BEZIER(S2)([hand6,hand4]))(domain2)

m1z = MAP(BEZIER(S2)([hand6z,hand5z]))(domain2)
m2z = MAP(BEZIER(S2)([hand6z,hand1z]))(domain2)
m3z = MAP(BEZIER(S2)([hand6z,hand2z]))(domain2)
m4z = MAP(BEZIER(S2)([hand6z,hand3z]))(domain2)
m5z = MAP(BEZIER(S2)([hand6z,hand4z]))(domain2)

m6 = MAP(BEZIER(S2)([hand1,hand1z]))(domain2)
m7 = MAP(BEZIER(S2)([hand2,hand2z]))(domain2)
m8 = MAP(BEZIER(S2)([hand3,hand3z]))(domain2)
m9 = MAP(BEZIER(S2)([hand4,hand4z]))(domain2)
m10 = MAP(BEZIER(S2)([hand5,hand5z]))(domain2)
m11 = MAP(BEZIER(S2)([hand6,hand6z]))(domain2)

hand = COLOR([0,1,55,1])(STRUCT([m1,m2,m3,m4,m5,m1z,m2z,m3z,m4z,m5z,m6,m7,m8,m9,m10,m11]))
hand_right = R([2,1])(-PI/12)(T([2])([1])(T([1])([1.5])(hand)))
hand_left = R([2,1])(PI/12)(T([2])([1])(T([1])([-2])(hand)))

/*THE FINAL BUBBLE MODEL*/
bubble_model = STRUCT([bodybubble,eyes,retinas,hand_right,hand_left])


/**********************************************THE WATER**********************************************/

/*THE FALLING WATER*/
water1a = BEZIER(S1)([[-0.7,0,0],[-0.7,1,0],[0.7,1,0],[0.7,0,0]])
water1b = BEZIER(S1)([[-0.7,0,0],[-0.7,-1,0],[0.7,-1,0],[0.7,0,0]])
water2a = BEZIER(S1)([[-0.7,0,3],[-0.7,1,3],[0.7,1,3],[0.7,0,3]])
water2b = BEZIER(S1)([[-0.7,0,3],[-0.7,-1,3],[0.7,-1,3],[0.7,0,3]])
water3a = BEZIER(S1)([[-0.7,0.5,4],[-0.7,1.3,3.5],[0.7,1.3,3.5],[0.7,0.5,4]])
water3b = BEZIER(S1)([[-0.7,0.5,4],[-0.7,-0.3,4.5],[0.7,0-0.3,4.5],[0.7,0.5,4]])
water4a = BEZIER(S1)([[-0.7,1,5],[-0.7,1.8,4.5],[0.7,1.8,4.5],[0.7,1,5]])
water4b = BEZIER(S1)([[-0.7,1,5],[-0.7,0.2,5.5],[0.7,0.2,5.5],[0.7,1,5]])
water5a = BEZIER(S1)([[-0.7,1.5,6],[-0.7,2.3,5.5],[0.7,2.3,5.5],[0.7,1.5,6]])
water5b = BEZIER(S1)([[-0.7,1.5,6],[-0.7,0.7,6.5],[0.7,0.7,6.5],[0.7,1.5,6]])
water6a = BEZIER(S1)([[-0.7,2,6.5],[-0.7,2.3,5.9],[0.7,2.3,5.9],[0.7,2,6.5]])
water6b = BEZIER(S1)([[-0.7,2,6.5],[-0.7,1.7,7.1],[0.7,1.7,7.1],[0.7,2,6.5]])
water7a = BEZIER(S1)([[-0.7,3,6.5],[-0.7,3,5.9],[0.7,3,5.9],[0.7,3,6.5]])
water7b = BEZIER(S1)([[-0.7,3,6.5],[-0.7,3,7.1],[0.7,3,7.1],[0.7,3,6.5]])
water8a = BEZIER(S1)([[-0.7,5,6.5],[-0.7,5,5.9],[0.7,5,5.9],[0.7,5,6.5]])
water8b = BEZIER(S1)([[-0.7,5,6.5],[-0.7,5,7.1],[0.7,5,7.1],[0.7,5,6.5]])

/*THE WATER IN THE GLASS*/
water9a = semicircle_a(4.4,3,2.5,0,0,0,0)
water9b = semicircle_b(4.4,3,2.5,0,0,0,0)
water10a = semicircle_a(4.2,2.8,2.8,0,0,0,0)
water10b = semicircle_b(4.2,2.8,2.8,0,0,0,0)
water11a = semicircle_a(4,2.6,3.1,0,0,0,0)
water11b = semicircle_b(4,2.6,3.1,0,0,0,0)
water12a = semicircle_a(3.5,2.1,3.5,0,0,0,0)
water12b = semicircle_b(3.5,2.1,3.5,0,0,0,0)
water13a = semicircle_a(2.9,1.8,4,0,0,0,0)
water13b = semicircle_b(2.9,1.8,4,0,0,0,0)
water14a = semicircle_a(1.3,0.8,4.3,0,0,0,0)
water14b = semicircle_b(1.3,0.8,4.3,0,0,0,0)
water15a = semicircle_a(0.8,0.5,4.35,0,0,0,0)
water15b = semicircle_b(0.8,0.5,4.35,0,0,0,0)

/*THE WATER IN THE BOTTLE*/
water16b = semicircle_b(0.6,2,0,0,0,0,0)
water17b = semicircle_b(4.3,2,5,0,0,0,0)
water18b = semicircle_a(0.6,0.1,0,0,0,0,0)
water19b = semicircle_a(4.3,0.1,5,0,0,0,0)

waterinside0 = MAP(BEZIER(S2)([water16b,water17b]))(domain2)
waterinside1 = MAP(BEZIER(S2)([water18b,water19b]))(domain2)
waterinside2 = MAP(BEZIER(S2)([water16b,water18b]))(domain2)
waterinside3 = MAP(BEZIER(S2)([water17b,water19b]))(domain2)
waterinside4 = MAP(BEZIER(S2)([water15b,water16b]))(domain2)
waterinside5 = MAP(BEZIER(S2)([water15a,water18b]))(domain2)
water_inside = COLOR([0,110,110,1])(STRUCT([waterinside0,waterinside1,waterinside2,waterinside3,waterinside4,waterinside5]))

/*THE FALLING DROPS*/
drop1 = BEZIER(S1)([[0,0,0],[2,1,0],[3,0.5,0],[3,0,0]])
drop2 = BEZIER(S1)([[0,0,0],[2,-1,0],[3,-0.5,0],[3,0,0]])
drop3 = BEZIER(S1)([[0,0,0.3],[2,1.5,0.3],[3,1,0.3],[3,0,0.3]])
drop4 = BEZIER(S1)([[0,0,0.3],[2,-1.5,0.3],[3,-1,0.3],[3,0,0.3]])
drop5 = BEZIER(S1)([[0,0,0.6],[2,1,0.6],[3,0.5,0.6],[3,0,0.6]])
drop6 = BEZIER(S1)([[0,0,0.6],[2,-1,0.6],[3,-0.5,0.6],[3,0,0.6]])
drop7 = BEZIER(S1)([[0,0,0],[2,0,-1],[3,0,-0.5],[3,0,0]])
drop8 = BEZIER(S1)([[0,0,0.6],[2,0,1.6],[3,0,1.1],[3,0,0.6]])

drop_map1 = MAP(BEZIER(S2)([drop1,drop3,drop5]))(domain2)
drop_map2 = MAP(BEZIER(S2)([drop2,drop4,drop6]))(domain2)
drop_map3 = MAP(BEZIER(S2)([drop1,drop7,drop2]))(domain2)
drop_map4 = MAP(BEZIER(S2)([drop5,drop8,drop6]))(domain2)
drop = S([0,1,2])([0.2,0.2,0.2])(STRUCT([drop_map1,drop_map2,drop_map3,drop_map4]))

drop_model1 = T([3])([4])(T([2])([-0.5])(R([2,3])(-2*PI/3)(R([2,1])([PI/2])(drop))))
drop_model2 = T([3])([2])(T([2])([-1.5])(R([2,3])(-PI/2)(R([2,1])([PI/2])(drop))))
drop_model3 = T([3])([5.5])(T([2])([3])(R([2,3])(-PI/2)(R([2,1])([PI/2])(drop))))

/*THE FINAL WATER MODELS*/
water_1 = MAP(BEZIER(S2)([water1a,water2a,water3a,water4a,water5a,water6a,water7a,water8a]))(domain2)
water_2 = MAP(BEZIER(S2)([water1b,water2b,water3b,water4b,water5b,water6b,water7b,water8b]))(domain2)
water_3 = MAP(BEZIER(S2)([water9a,water10a,water11a,water12a,water13a,water14a,water15a]))(domain2)
water_4 = MAP(BEZIER(S2)([water9b,water10b,water11b,water12b,water13b,water14b,water15b]))(domain2)
water_5 = MAP(BEZIER(S2)([water15a,water15b]))(domain2)

water_model1 = STRUCT([water_1,water_2])
water_model2 = S([0,1,2])([0.9,0.9,1])(COLOR([0,110,110,1])(STRUCT([water_3,water_4,water_5])))

water_model = COLOR([0,110,110,1])(STRUCT([water_model1,drop_model1,drop_model2,drop_model3]))

/**********************************************THE GLASS***************************************************************/

/*THE BODY GLASS */
glass0a = semicircle_a(4.2,2.6,0.1,0,0,0,0)
glass0b = semicircle_b(4.2,2.6,0.1,0,0,0,0)
glass1a = semicircle_a(4,2.5,0,0,0,0,0)
glass1b = semicircle_b(4,2.5,0,0,0,0,0)
glass2a = semicircle_a(4,2.5,0.2,0,0,0,0)
glass2b = semicircle_b(4,2.5,0.2,0,0,0,0)
glass3a = semicircle_a(3.8,2.25,0.3,0,0,0,0)
glass3b = semicircle_b(3.8,2.25,0.3,0,0,0,0)
glass4a = semicircle_a(3.8,2.25,1.5,0,0,0,0)
glass4b = semicircle_b(3.8,2.25,1.5,0,0,0,0)
glass5a = semicircle_a(4,2.6,2,0,0,0,0)
glass5b = semicircle_b(4,2.6,2,0,0,0,0)
glass6a = semicircle_a(4.2,2.8,2.2,0,0,0,0)
glass6b = semicircle_b(4.2,2.8,2.2,0,0,0,0)
glass7a = semicircle_a(4.4,3,2.5,0,0,0,0)
glass7b = semicircle_b(4.4,3,2.5,0,0,0,0)
glass8a = semicircle_a(4.2,2.8,2.8,0,0,0,0)
glass8b = semicircle_b(4.2,2.8,2.8,0,0,0,0)
glass9a = semicircle_a(4,2.6,3.1,0,0,0,0)
glass9b = semicircle_b(4,2.6,3.1,0,0,0,0)
glass10a = semicircle_a(3.5,2.1,3.5,0,0,0,0)
glass10b = semicircle_b(3.5,2.1,3.5,0,0,0,0)
glass11a = semicircle_a(2.9,1.8,4,0,0,0,0)
glass11b = semicircle_b(2.9,1.8,4,0,0,0,0)
glass12a = semicircle_a(1.3,0.8,4.3,0,0,0,0)
glass12b = semicircle_b(1.3,0.8,4.3,0,0,0,0)
glass13a = semicircle_a(0.8,0.5,4.4,0,0,0,0)
glass13b = semicircle_b(0.8,0.5,4.4,0,0,0,0)

/*THE GLASS STICK*/
stick0a = semicircle_a(0.8,0.5,4.4,0,0,0,0)
stick0b = semicircle_b(0.8,0.5,4.4,0,0,0,0)
stick1a = semicircle_a(0.5,0.3,4.7,0,0,0,0)
stick1b = semicircle_b(0.5,0.3,4.7,0,0,0,0)
stick2a = semicircle_a(0.5,0.3,6.5,0,0,0,0)
stick2b = semicircle_b(0.5,0.3,6.5,0,0,0,0)

/*THE GLASS BASE*/
base1a = semicircle_a(0.8,0.5,6.7,0,0,0,0)
base1b = semicircle_b(0.8,0.5,6.7,0,0,0,0)
base2a = semicircle_a(1.2,0.8,6.8,0,0,0,0)
base2b = semicircle_b(1.2,0.8,6.8,0,0,0,0)
base3a = semicircle_a(2,1.4,7,0,0,0,0)
base3b = semicircle_b(2,1.4,7,0,0,0,0)
base4a = semicircle_a(3.5,2.3,7,0,0,0,0)
base4b = semicircle_b(3.5,2.3,7,0,0,0,0)

/*THE CUP SURFACES*/
glass_map1a = MAP(BEZIER(S2)([glass1a,glass0a,glass2a]))(domain2)
glass_map2a = MAP(BEZIER(S2)([glass2a,glass3a,glass4a,glass5a,glass6a,
              glass7a,glass8a,glass9a,glass10a,glass11a,glass12a,glass13a]))(domain2)
glass_map1b = MAP(BEZIER(S2)([glass1b,glass0b,glass2b]))(domain2)
glass_map2b = MAP(BEZIER(S2)([glass2b,glass3b,glass4b,glass5b,glass6b,
              glass7b,glass8b,glass9b,glass10b,glass11b,glass12b,glass13b]))(domain2)
glass_map3 = MAP(BEZIER(S2)([glass13a,glass13b]))(domain2)

/*THE STICK SURFACES*/
stick_map1 = MAP(BEZIER(S2)([stick1a,stick1b]))(domain2)
stick_map2 = MAP(BEZIER(S2)([stick2b,stick2b]))(domain2)
stick_map3 = MAP(BEZIER(S2)([stick1a,stick2a]))(domain2)
stick_map4 = MAP(BEZIER(S2)([stick1b,stick2b]))(domain2)
stick_map5 = MAP(BEZIER(S2)([stick0a,stick0b]))(domain2)
stick_map6 = MAP(BEZIER(S2)([stick0a,stick1a]))(domain2)
stick_map7 = MAP(BEZIER(S2)([stick0b,stick1b]))(domain2)
stick_map8 = MAP(BEZIER(S2)([stick2a,stick2b]))(domain2)

/*THE BASE SURFACES*/
base_map1 = MAP(BEZIER(S2)([stick2a,base1a]))(domain2)
base_map2 = MAP(BEZIER(S2)([stick2b,base1b]))(domain2)
base_map3 = MAP(BEZIER(S2)([base1a,base2a,base3a,base4a]))(domain2)
base_map4 = MAP(BEZIER(S2)([base1b,base2b,base3b,base4b]))(domain2)

/*THE FINAL GLASS MODEL*/
closurecup_model = COLOR([0,0,1,1])(STRUCT([glass_map3]))
base_model = COLOR([0,1,10,0.6])(STRUCT([base_map1,base_map2,base_map3,base_map4]))
rim_model =  COLOR([255,215,0])(STRUCT([glass_map1a,glass_map1b]))
glasscup_model = COLOR([0,1,10,0.6])(STRUCT([glass_map2a,glass_map2b]))
stick_model = COLOR([0,1,10,0.6])(STRUCT([stick_map1,stick_map2,stick_map3,stick_map4,
stick_map5,stick_map6,stick_map7,stick_map8]))

glass_model = STRUCT([closurecup_model,glasscup_model,stick_model,base_model,rim_model,water_model2])


/**********************************************THE FINAL MODEL**********************************************/

/*THE BOTTLE, THE BUBBLE, THE GLASS, THE WATER*/
bubble_rotated = T([2])([7])(T([1])([4])(R([2,3])(PI)(R([1,2])(PI/2)(bubble_model))))
waterinside_rotated = T([1])([-4])(T([2])([-3])(R([1,2])(PI/12)(R([3,2])(PI/2)(R([2,1])(PI/2)(S([0,1,2])([0.6,0.6,0.6])(water_inside))))))
cap_rotated = T([2])([-7])(T([1])([7])(cap))
water_rotated = S([1,2,3])([0.6,0.6,0.6])(T([1])([3])(R([2,1])(PI)(R([3,1])(PI/2)(water_model))))
glass_rotated = R([3,1])(PI/2)(S([0,1,2])([0.9,0.9,0.9])(glass_model))
bottle_rotated = T([1])([-6])(T([2])([-3])(R([2,1])(-2*PI/3.5)(bottle_model)))

model = STRUCT([bottle_rotated, bubble_rotated,glass_rotated, water_rotated, cap_rotated, waterinside_rotated])

