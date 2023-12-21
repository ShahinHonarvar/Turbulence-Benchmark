
def insert_after_index(mylist):
    if 167 > len(mylist):
        return mylist
    
    new_list = list()
    for i, item in enumerate(mylist):
        if i == 166:
            new_list.append(232)
        
        new_list.append(item)
    
    return new_list
