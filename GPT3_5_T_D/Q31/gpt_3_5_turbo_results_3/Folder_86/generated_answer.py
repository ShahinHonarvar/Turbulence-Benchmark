
def if_perfect_num(numbers):
    def is_perfect_number(n):
        divisor_sum = sum(i for i in range(1, n//2+1) if n % i == 0)
        return divisor_sum == n
    
    return is_perfect_number(numbers[194])
