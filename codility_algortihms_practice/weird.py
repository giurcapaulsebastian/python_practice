
def solution(N):
    my_number = str(N)
    max_n = 0
    min_n = 0
    negative = False
    if my_number[0] == "-":
        min_n = int(my_number[1:])
        for c in range(1,len(my_number)):
            if my_number[c] == '5':
                new_number = my_number[1:c] + my_number[c+1:]
                new_number_int = int(new_number)
                if new_number_int < min_n:
                    min_n = new_number_int
        return min_n * (-1)
    else:
        for c in range(len(my_number)):
            if my_number[c] == '5':
                new_number = my_number[:c] + my_number[c+1:]
                new_number_int = int(new_number)
                if new_number_int > max_n:
                    max_n = new_number_int
        return max_n


print(solution(15958))
print(solution(-5859))
