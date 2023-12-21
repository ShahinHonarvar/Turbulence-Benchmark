
def if_perfect_num(numbers):
    def is_perfect(num):
        divisors = [x for x in range(1, num) if num % x == 0]
        return sum(divisors) == num
    
    if len(numbers) > 37 and is_perfect(numbers[37]):
        return True
    else:
        return False
