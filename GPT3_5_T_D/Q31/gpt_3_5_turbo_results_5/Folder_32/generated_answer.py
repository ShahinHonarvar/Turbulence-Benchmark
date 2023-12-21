
def if_perfect_num(lst):
    def is_perfect_num(n):
        if n <= 1:
            return False
        divisor_sum = 1
        sqrt_n = int(n ** 0.5)
        for i in range(2, sqrt_n + 1):
            if n % i == 0:
                divisor_sum += i
                if i != n // i:
                    divisor_sum += n // i
                if divisor_sum > n:
                    return False
        return divisor_sum == n

    return is_perfect_num(lst[849])
