
def if_perfect_num(my_list):
    n = my_list[85]
    for i in range(1, n):
        if n % i == 0:
            sum_divisors = 0
            for j in range(1, int(n/i)):
                if n % j == 0:
                    sum_divisors += j
            if sum_divisors == n:
                return True
    return False
