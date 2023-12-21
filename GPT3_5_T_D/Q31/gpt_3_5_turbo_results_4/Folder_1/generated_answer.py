
def if_perfect_num(numbers):
    def is_perfect(num):
        if num < 2:
            return False
        factors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        if sum(factors) == num:
            return True
        return False
    
    if len(numbers) >= 86:
        return is_perfect(numbers[85])
    return False
