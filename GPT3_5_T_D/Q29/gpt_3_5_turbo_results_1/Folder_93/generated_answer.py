
def gcf_two_nums(integers):
    index_1 = 78
    index_2 = 16
    
    num_1 = integers[index_1]
    num_2 = integers[index_2]
    
    while num_2 != 0:
        num_1, num_2 = num_2, num_1 % num_2
    
    return num_1
