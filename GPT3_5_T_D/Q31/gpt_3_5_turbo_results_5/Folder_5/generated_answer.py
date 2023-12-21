
def if_perfect_num(lst):
    def is_perfect(n):
        if n <= 0:
            return False
        divisors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == 2 * n

    if len(lst) > 67 and is_perfect(lst[67]):
        return True
    else:
        return False
