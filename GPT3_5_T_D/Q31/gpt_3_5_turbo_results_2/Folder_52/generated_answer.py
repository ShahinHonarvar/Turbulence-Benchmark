
def if_perfect_num(lst):
    num = lst[478]
    divisors = [1]
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            divisors.append(num // i)
    divisor_sum = sum(divisors)
    if divisor_sum == num:
        return True
    else:
        return False
