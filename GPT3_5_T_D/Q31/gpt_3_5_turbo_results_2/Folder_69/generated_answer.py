
def if_perfect_num(lst):
    def is_perfect_num(n):
        sum_factors = 1
        i = 2
        while i * i <= n:
            if n % i == 0:
                sum_factors += i
                if i != n // i:
                    sum_factors += n // i
            i += 1
        return sum_factors == n

    if len(lst) >= 460:
        return is_perfect_num(lst[459])
    else:
        return False
