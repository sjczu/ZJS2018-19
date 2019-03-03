ab=[True,False]
bc=[True,False]
cd=[True,False]
de=[True,False]
ef=[True,False]

for a in ab:
    for b in bc:
        for c in cd:
            for d in de:
                for e in ef:
                    w1=a or b and c or d and not e
                    #w2=a or (b and c) or (d and not e)
                    #w2=a or (b and c or d) and not e
                    #w2=((a or b and c) or d) and not e
                    #w2=a and (b or c) and not (d or e)
                    w2=(a and not b) or not c or (d or e)
                    if not w1==w2:
                        print (a,b,c,d,e)