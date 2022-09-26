#Lambdas

def func(x):
    return x+5

print(func(2))

func2 = lambda x : x+5
print(func2(2))

func3 = lambda x,y : x+y
print(func3(2,3))

a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x:x+5, a))

print(newList)

newList = list(filter(lambda x: x%2==0,a))
print(newList)