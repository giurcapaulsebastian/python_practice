# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    my_arrows = {
        "^":0,
        "v":0,
        "<":0,
        ">":0
    }
    
    most_occurances = 0
    
    for i in S:
        my_arrows[i] +=1
        if my_arrows[i] > most_occurances:
            most_occurances = my_arrows[i]
    
    return len(S) - most_occurances


print(solution("^vv<v"))