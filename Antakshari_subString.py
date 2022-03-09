seq= 'mango,orange,banana,atom,man,name,elastic,cough,hot'
list_seq=seq.split(',')
#print(list1)

temp=''
count=1
list_count=[]
for i in range (len(list_seq)):
        current_temp=list_seq[i][0]
        #print(current_temp)
        print(current_temp,temp)
        if(current_temp==temp):
            count+=1
        else:
            list_count.append(count)
            count=1
        if(i==(len(list_seq)-1) and count!=1):
           list_count.append(count)
            
        temp=list_seq[i][-1]


print(max(list_count))