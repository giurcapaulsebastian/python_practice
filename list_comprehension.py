my_list = [1,2,3]
new_list = [x*2 for x in my_list]
print(new_list)

users = [{'name': 'Manuel', 'age':31}, {'name': 'Paul', 'age':30}, {'name': 'Seb', 'age':38}]
user_name = [user["name"] for user in users if user["age"] > 30]
print(user_name)


user_groups = [
    [
        {'name':'Manuel', 'age':31},
        {'name':'Max', 'age':30}
    ],
    [
        {'name':'Sarah', 'age':29},
        {'name':'Julie', 'age':32}
    ]
]

user_name = [person['name'] for group in user_groups for person in group]
print(user_name)

result = [(letter,num) for letter in "abcd" for num in range(4)]
print(result)

print(__name__)

print(globals())
print(__file__)

nums = [1,2,3,4,5,6,7,8,9,10]

my_gen = (n*n for n in nums)

print(my_gen)
for i in my_gen:
    print(i)
