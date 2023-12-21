
def if_perfect_num(my_list):
    # Check if the list has at least 126 elements
    if len(my_list) < 126:
        return False

    # Check if the element at index 126 is a perfect number
    else:
        element = my_list[126]
        if element == 0:
            return False

        divisors = [i for i in range(1, element // 2 + 1) if element % i == 0]
        sum_of_divisors = sum(divisors)
        if sum_of_divisors == element:
            return True

        else:

            return False
