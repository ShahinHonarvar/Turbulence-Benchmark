
def find_second_largest_num(my_list):
    if len(my_list) < 5:
        return None
    
    second_largest = None
    largest = my_list[0]
    
    for i in range(1, len(my_list)):
        num = my_list[i]
        
        if num > largest:
            second_largest = largest
            largest = num
            
    return second_largest
