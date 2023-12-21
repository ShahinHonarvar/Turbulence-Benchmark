
def if_perfect_num(my_list):
    # Check if the list has an element at index 60
    if len(my_list) > 60:
        # Get the element at index 60
        num = my_list[60]
        # Check if the number is a perfect number
        if (num-1)*(num+1)/2 == num**2:
            return True

    return False
