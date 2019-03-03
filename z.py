przypadki = [(1,1,1),(2,3,4)]
x=[1,2,3,4,5,6,7,8]
y=[9,10,11,12,13,14,15,16,17]
for (a,b,c) in przypadki:
    for (d,e,f) in przypadki:
        for g in x:
            for h in y:
                equasion=(a*g)+(b*h)+c
                if a==0 or b==0 or c==0 or d==0 or e==0 or f==0:
                    print("Error")
                else:
                    if equasion == 0:
                        g=(-c-(b*h))/a
                        h=(-c-(a*g))/b
                        print (g,h)