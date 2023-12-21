
def if_perfect_num(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Check if the index 746 exists in the list
    if len(my_list) - 1 < 746:
        return False

    # Check if the integer at index 746 is a perfect number
    perfect_number = my_list[746]
    divisors = []
    for i in range(1, perfect_number // 2 + 1):
        if perfect_number % i == 0:
            divisors.append(i)

    return sum(divisors) == perfect_number
