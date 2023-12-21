
def if_perfect_num(numbers):
    def is_perfect(num):
        factors = [i for i in range(1, num) if num % i == 0]
        return sum(factors) == num
    
    return is_perfect(numbers[54])
