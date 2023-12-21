
def if_perfect_num(numbers):
    def is_perfect(num):
        if num < 6:
            return False
        factors_sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors_sum += i
                if i != num // i:
                    factors_sum += num // i
        return factors_sum == num
    
    if len(numbers) > 993:
        return is_perfect(numbers[993])
    else:
        return False
