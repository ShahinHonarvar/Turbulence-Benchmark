
def find_second_smallest_num(numbers):
    if len(numbers)>=71:  
        sublist= numbers[70:201]
        sublist.sort()
        if len(sublist)>1:
            return sublist[1]
    return None
