
def if_perfect_num(lst):
    def is_perfect(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n

    if len(lst) > 90:
        return is_perfect(lst[90])
    else:
        return False
