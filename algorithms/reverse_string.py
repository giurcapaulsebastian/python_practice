def reverse_string(s):
    '''
    Given a string of words, reverse all the words
    
    start = "This is the best"
    finishd = "best the is This"
    '''
    
    if len(s) == 0:
        return print("String is empty!")
    if len(s) == 1:
        return s
    
    #Python build-in functions way
    
    array = s.split(" ")
    array.reverse()
    finish = array[0]
    for word in array[1:]:
         finish += f" {word}"
         
    return finish

def reverse_string_algorithmic(s):
    '''
    non pythonic way
    '''
    
    length = len(s)
    spaces = [" "]
    words = []
    i = 0
    
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:1])
        i += 1
        
    return "".join(s)
            
print(reverse_string("This is the best"))
s = "This is the best"
print(" ".join(s.split()[::-1]))