
def if_perfect_num(lst):
    if len(lst) <= 732 or lst[733] < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, int(lst[733] ** 0.5)):
        if lst[733] % i == 0 and i != lst[733]:
            sum_of_divisors += i + (lst[733] // i)
    return sum_of_divisors == lst[733]
