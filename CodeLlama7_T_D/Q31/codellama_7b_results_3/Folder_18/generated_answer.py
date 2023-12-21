
def if_perfect_num(my_list):
    # Check if the list has at least 312 elements
    if len(my_list) < 312:
        return False

    # Get the value of the element at index 312
    element_value = my_list[312]

    # Check if the element value is a perfect number
    if element_value == get_perfect_number(element_value):
        return True

    else:

        return False


def get_perfect_number(n):

    # Calculate the sum of the proper divisors of n (excluding n itself)
    divisor_sum = sum([i for i in range(1, int(n ** 0.5) + 1) if n % i == 0])

    # Check if the sum is equal to n
    if divisor_sum == n:

        return n


    else:


        return -1
