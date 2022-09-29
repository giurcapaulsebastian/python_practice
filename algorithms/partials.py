for _ in range(1,10,2):
    print(_)
    
        

tup1 = (1,2,3)
tup2 = (3,4,5)

l1 = [1,2,3]
l2 = [3,4,5]

dicti = dict(zip(tup1,tup2))

print(zip(tup1,tup2))

for item in zip(tup1,tup2):
    print(item)
    
for item in zip(l1,l2):
    print(item)
print(type(item))

print(dict)


def my_generator(): 
    for i in range(1,5):
        yield i*i
        
gen = my_generator()

x = gen.__next__()
print(x)