
def if_perfect_num(numbers):
    def is_perfect(num):
        factors = []
        for i in range(1, int(num/2)+1):
            if num % i == 0:
                factors.append(i)
        if sum(factors) == num:
            return True
        return False
    
    return is_perfect(numbers[247])
