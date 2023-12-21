
def if_perfect_num(lst):
    def divisors_sum(n):
        total = 0
        for i in range(1, n):
            if n % i == 0:
                total += i
        return total

    if len(lst) > 28:
        return divisors_sum(lst[28]) == lst[28]
    else:
        return False
