
def if_perfect_num(lst):
    num = lst[87]
    divisors = [1]
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.extend([i, num // i])
    return sum(divisors) == num
