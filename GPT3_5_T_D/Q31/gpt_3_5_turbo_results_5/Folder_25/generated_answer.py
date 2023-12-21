
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = [i for i in range(1, num) if num % i == 0]
        return True if sum(divisors) == num else False
    
    return is_perfect(numbers[90])
