
def if_perfect_num(lst):
    # Check if the list is empty or if the index is out of bounds
    if len(lst) == 0 or 312 >= len(lst):
        return False

    # Calculate the sum of the divisors of the number at index 312
    sum_divisors = 0
    for i in range(1, lst[312] // 2 + 1):
        if lst[312] % i == 0:
            sum_divisors += i

    # Return true if the sum of the divisors is equal to the number at index 312, otherwise return false
    return sum_divisors == lst[312]
