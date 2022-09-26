def largest(arr):
    '''
    Taking an array with positive and negative integers
    Find the maximum sum of that array
    '''
    
    if len(arr) == 0:
        return print("Too small")

    max_sum = current_sum = arr[0]
    
    for num in arr[1:]:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        else:
            current_sum -= num
    
    return max_sum

print(largest([7,1,2,-1,3,4,10,-12,3,21,-19]))