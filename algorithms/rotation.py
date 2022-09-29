def rotation(list1,list2):
    if len(list1) != len(list2):
        return False
    
    key = list1[0]
    key_index = 0
    
    for i in range(len(list2)):
        if list2[i] == key:
            key_index = i