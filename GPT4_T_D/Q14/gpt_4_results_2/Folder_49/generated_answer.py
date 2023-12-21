
def find_second_smallest_num(lst):
    if len(lst) < 81:
        return None
    
    second_smallest = sorted(lst[80:201], reverse=False)
    
    if len(second_smallest) < 2:
        return None
    
    return second_smallest[1]
