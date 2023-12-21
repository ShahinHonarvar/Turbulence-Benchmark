
def if_perfect_num(lst):
    def is_perfect(n):
        divisors = [x for x in range(1, n) if n % x == 0]
        return sum(divisors) == n

    return is_perfect(lst[24])
