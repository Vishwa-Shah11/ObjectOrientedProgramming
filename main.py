def is_function(domain, co_domain, fun):
    flag = False
    if all(i in fun.keys() for i in domain):
    #for i in domain:
        #if (i in fun.keys()):#have to check for every element. this is checking for any element
            #print('in domain')
            #continue #this is for checking every element, but solution not working!!
        flag = True
    if all(i in domain for i in fun.keys()):
    #for j in fun.keys():
        #if (j in domain):#have to check for every element. this is checking for any element
            #print('IN fun.KEYS')
            #continue
        flag = True
    if all(i in fun.values() for i in co_domain):
    #for k in co_domain:
        #if (k in fun.values()):#have to check for every element. this is checking for any element
            #print('in CO_DOMAIN')
            #continue
        flag = True

    return flag

print(is_function([1,2,3], [5,6,7], {1:5, 2:6, 4:7}))