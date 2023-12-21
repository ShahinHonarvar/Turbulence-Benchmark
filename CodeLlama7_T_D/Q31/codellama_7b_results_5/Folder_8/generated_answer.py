
def if_perfect_num(my_list):
    # Check if the list has at least 50 elements
    if len(my_list) < 50:
        return False

    # Get the value of the element at index 49
    element_value = my_list[49]

    # Check if the element value is a perfect number
    if is_perfect_num(element_value):
        return True

    else:

        return False

def is_perfect_num(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i

    if sum == n - 1:

        return True

    else:

        return False
