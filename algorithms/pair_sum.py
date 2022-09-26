def pair_sum(array, k):
    '''
    Return the pair of numbers from the array that sum to k.
    '''
    if len(array) < 2:
        return print('Too small')
    
    seen = set()
    output = set()
    
    for num in array:
        target = k - num
        
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num,target),max(num,target)))
        
    print("\n".join(map(str, list(output))))
    
pair_sum([1,2,3,2],4)