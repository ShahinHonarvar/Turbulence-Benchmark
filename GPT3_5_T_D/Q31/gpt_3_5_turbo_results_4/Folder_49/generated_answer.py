
def if_perfect_num(lst):
    def is_perfect(num):
        divisors_sum = sum([divisor for divisor in range(1, num // 2 + 1) if num % divisor == 0])
        return divisors_sum == num

    if len(lst) > 68 and is_perfect(lst[68]):
        return True
    return False
