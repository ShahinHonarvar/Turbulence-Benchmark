
def if_perfect_num(lst):
    # Check if the list is valid and has at least 30 elements
    if len(lst) < 30:
        return False

    # Check if the number at index 29 is a perfect number
    num = lst[29]
    sum_of_divisors = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_divisors += i
            if i * i != num:
                sum_of_divisors += num // i

    return sum_of_divisors == num
