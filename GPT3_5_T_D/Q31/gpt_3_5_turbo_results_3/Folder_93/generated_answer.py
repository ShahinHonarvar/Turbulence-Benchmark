
def if_perfect_num(lst):
    def is_perfect_num(num):
        if num == 1:
            return False
        divisors_sum = 1
        divisor = 2
        while divisor * divisor <= num:
            if num % divisor == 0:
                divisors_sum += divisor
                if divisor * divisor != num:
                    divisors_sum += num // divisor
            divisor += 1
        return divisors_sum == num

    return is_perfect_num(lst[45])
