def seperator(x):
    global zoj , fard
    zoj = tuple()
    fard =tuple()
    
    for i in x:
        if x % 2 == 0:
            zoj.append(x)
        else:
            fard.append(x)
    return(zoj,fard)
num = input()
x = tuple(map(int, num.split(',')))
seperator (x)
print(zoj,fard)





    