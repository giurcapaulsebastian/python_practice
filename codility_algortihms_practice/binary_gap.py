#A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. 
# The number 20 has binary representation 10100 and contains one binary gap of length 1. 
# The number 15 has binary representation 1111 and has no binary gaps. 
# The number 32 has binary representation 100000 and has no binary gaps.

def solution(N):
    if N < 5:
        return 0
    
    max_gap = 0
    current_gap = 0
    
    while N:
        if N%2 == 1 and (N//2)%2 ==0:
            N=N//2
            while(N%2==0 and N//2 !=0):
                #we start to check
                N=N//2
                current_gap += 1
            if current_gap > max_gap:
                max_gap = current_gap
            current_gap = 0
        else:
            N=N//2
    return max_gap


print(solution(529))
print(solution(20)) 