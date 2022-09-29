

def solution(A):
    # write your code in Python 3.6
    A.sort()
    current = -1
    print(A)
    for i in (len(A)-2,2):
        current = A[i]
        if i == len(A)-2:
            return A[len(A)]
        if A[i] == A[i+1]:
            current = -1
        if A[i] != A[i+1] and current == -1:
            return A[i+1]
        
    
    
print(solution([9, 3, 9, 3, 9, 7, 9]))