
def if_perfect_num(numbers):
    def is_perfect(num):
        if num <= 1:
            return False
        factor_sum = sum(i for i in range(1, num) if num % i == 0)
        return factor_sum == num
    
    return is_perfect(numbers[21])
