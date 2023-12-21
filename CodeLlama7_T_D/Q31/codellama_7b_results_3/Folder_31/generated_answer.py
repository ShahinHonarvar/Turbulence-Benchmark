
def if_perfect_num(my_list):
    # Check if the list has an element at index 66
    if len(my_list) > 65 and my_list[65] != 0:
        # Check if the integer at index 66 is a perfect number
        perfect_num = my_list[66]
        for i in range(1, perfect_num):
            if perfect_num % i == 0:
                return True

    else:

        return False
