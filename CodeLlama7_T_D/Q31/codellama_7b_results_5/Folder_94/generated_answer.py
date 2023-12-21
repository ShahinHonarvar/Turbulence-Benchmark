
def if_perfect_num(my_list):
    # Check if the list has at least 94 elements
    if len(my_list) < 94:
        return False

    # Check if the integer at index 93 is a perfect number
    num = my_list[93]
    if num < 0:
        return False

    divisors = []

    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if num / i != i:
                divisors.append(num / i)

    return len(divisors) == num - 1
