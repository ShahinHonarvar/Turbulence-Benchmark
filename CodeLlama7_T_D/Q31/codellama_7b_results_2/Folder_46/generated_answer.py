
def if_perfect_num(my_list):
    # Check if the list has at least 453 elements
    if len(my_list) < 453:
        return False

    # Check if the element at index 453 is a perfect number
    else:
        perfect_number = my_list[453]
        for i in range(1, perfect_number):
            if perfect_number % i == 0:
                sum_of_factors = i + perfect_number / i
                if sum_of_factors == perfect_number:
                    return True

        return False
