
def if_perfect_num(lst):
    def is_perfect_num(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        if sum(divisors) == n:
            return True
        return False

    if len(lst) >= 100:
        return is_perfect_num(lst[99])
    return False
