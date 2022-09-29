# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def binary_to_decimal(S):
    power_of_2 = 0
    decimal_number = 0
    for c in S[::-1]:
        if c!='0':
            decimal_number = 2**power_of_2 + decimal_number
        power_of_2 +=1
        print(decimal_number)
    return decimal_number

def solution(S):
    # write your code in Python 3.6
    decimal_number = binary_to_decimal(S)
    
    # number_of_operations = 0
    # while decimal_number != 0:
    #     if decimal_number%2 == 0:
    #         decimal_number = decimal_number/2
    #         number_of_operations += 1
    #     else:
    #         decimal_number -= 1
    #         number_of_operations +=1

    # return number_of_operations

solution("011100")