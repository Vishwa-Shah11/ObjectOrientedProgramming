#str = input().split(',')
str = 'one,two,order,real,long,tight,tree,cool,lot,trouble'
my_lst = str.split(',')
print(my_lst)
count = 0

for i in my_lst:
    next_word = my_lst[my_lst.index(i) + 1]
    #print(next_word)
    #print(i)
    #print(i[-1])
    #print(next_word[0])
    #print(i)
    #print(i, next_word)
    if (i[-1] == next_word[0]):
        count += 1
print(count)
   