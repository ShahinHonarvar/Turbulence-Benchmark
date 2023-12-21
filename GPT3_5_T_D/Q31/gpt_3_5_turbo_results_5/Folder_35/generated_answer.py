
def if_perfect_num(numbers):
    def is_perfect_number(num):
        factors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.extend([i, num // i])
        return sum(factors) == num
    
    return is_perfect_number(numbers[993]) if 0 <= 993 < len(numbers) else False
