
def if_perfect_num(numbers):
    def is_perfect(num):
        if num < 2:
            return False
        factors = [1]
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        
        return sum(factors) == num
    
    if len(numbers) > 96:
        return is_perfect(numbers[96])
    else:
        return False
