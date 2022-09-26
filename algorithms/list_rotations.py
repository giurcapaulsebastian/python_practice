#Check if list1 is a rotation or list2


def rotation(list1,list2):
    if (len(list1) != len(list2)):
        return False
    
    
    pass

l1 = [1,2,3,4,5]
l2 = [3,4,5,1,2]

combined = [x for x in l1[2:]] + [x for x in l1[:2]]
print(combined)