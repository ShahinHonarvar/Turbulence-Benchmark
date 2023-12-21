
def if_perfect_num(lst):
    # Check if the list has 93 elements
    if len(lst) != 93:
        return False

    # Get the value of the number at index 92
    num = lst[92]

    # Check if the number is a perfect number
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors = i + num / i
            if sum_divisors == num:
                return True

    # If the number is not a perfect number, return False
    return False
