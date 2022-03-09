def is_function(domain, co_domain, fun):
    flag = True
    domain.sort()
    l1 = list(fun.keys())
    l1.sort()
    l2 = list(fun.values())
    
    if (domain == l1):
        flag = True
    else:
        flag = False

    if ((set(l2)).issubset(set(co_domain)) and flag == True):
        flag = True
    else:
        flag = False
    '''
    for i in domain:
        if (i in fun.keys()):
            flag = True
            print(flag)
    
    for j in fun.keys():
        if (j in domain):
            flag = True
            print(flag)
  
    for k in co_domain:
        if (k in fun.values()):
            flag = True
            print(flag)
    '''
    return flag

print(is_function([1,2,3], [5,6,7], {1:5, 2:6, 4:7}))