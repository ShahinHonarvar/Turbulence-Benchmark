
def if_perfect_num(numbers):
    def is_perfect_num(n):
        if n <= 1:
            return False
        divisor_sum = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisor_sum += i
                if i != n // i:
                    divisor_sum += n // i
        if divisor_sum == n:
            return True
        return False
    
    if len(numbers) <= 69:
        return False
    return is_perfect_num(numbers[69])
