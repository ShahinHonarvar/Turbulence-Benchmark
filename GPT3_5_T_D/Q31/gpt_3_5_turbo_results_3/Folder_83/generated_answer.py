
def if_perfect_num(lst):
    def is_perfect_num(n):
        divisors_sum = 0
        for i in range(1, n):
            if n % i == 0:
                divisors_sum += i
        return divisors_sum == n

    return is_perfect_num(lst[95])
