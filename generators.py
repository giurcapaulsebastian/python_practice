x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i: i**2, x)

for n in y:
    print(n)
    
def gen(n):
    for i in range(n):
        yield i

for i in gen(5):
    print(i)
    

gen = ((x,x) for x in range(5))

for n in gen:
    print(n)
    
D = ((t,t) for t in [1,2,3,4,5] )
print(D)

for d in D:
    print(d)