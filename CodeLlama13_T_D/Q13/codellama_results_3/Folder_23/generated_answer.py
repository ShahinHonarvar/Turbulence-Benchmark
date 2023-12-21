
def find_second_largest_num(my_list):
    my_list = sorted(my_list)
    second_largest = None
    for i in range(52, 71+1):
        if my_list[i] > my_list[i-1]:
            second_largest = my_list[i]
            break
    return second_largest
