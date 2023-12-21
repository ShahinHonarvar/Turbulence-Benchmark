
def if_perfect_num(lst):
    def is_perfect(num):
        if num < 2:
            return False

        divisors_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if num // i != i:
                    divisors_sum += num // i

        return divisors_sum == num

    return is_perfect(lst[56])
