
def if_perfect_num(lst):
    num = lst[844]
    sum_of_divisors = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum_of_divisors += i
            if i != num // i:
                sum_of_divisors += num // i
        i += 1
    return sum_of_divisors == num
