
def if_perfect_num(my_list):
    # Check if the list has an element at index 845
    if len(my_list) > 845:
        # Get the value of the element at index 845
        num = my_list[845]
        # Calculate the sum of its factors
        factor_sum = sum([i for i in range(1, int(num ** 0.5) + 1) if num % i == 0])
        # Check if the sum of its factors is equal to the number itself
        if factor_sum == num:
            return True
        else:
            return False
    else:
        return False
