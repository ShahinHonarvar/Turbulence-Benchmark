
def if_perfect_num(lst):
    num = lst[73]
    if num < 1:
        return False
    divisors = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sum(divisors) == 2 * num
