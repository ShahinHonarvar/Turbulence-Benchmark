
def find_second_smallest_num(lst):
    if len(lst[40:81]) < 2: 
        return None
    
    lst = sorted(lst[40:81])
    return lst[1]
