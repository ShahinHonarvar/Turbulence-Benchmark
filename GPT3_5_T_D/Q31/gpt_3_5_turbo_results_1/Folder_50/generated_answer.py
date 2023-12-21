
def if_perfect_num(lst):
    def is_perfect_num(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return sum(divisors) == n

    return is_perfect_num(lst[40])
