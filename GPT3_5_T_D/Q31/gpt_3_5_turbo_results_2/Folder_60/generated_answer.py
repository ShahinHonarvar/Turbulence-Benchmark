
def if_perfect_num(lst):
    def is_perfect_num(n):
        if n <= 1:
            return False
        divisors_sum = 1
        sqrt_n = int(n ** 0.5)
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                divisors_sum += i
                if i != n // i:
                    divisors_sum += n // i
        return divisors_sum == n

    if len(lst) <= 88:
        return False
    return is_perfect_num(lst[88])
