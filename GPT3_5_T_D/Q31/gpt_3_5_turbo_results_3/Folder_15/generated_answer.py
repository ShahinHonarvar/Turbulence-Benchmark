
def if_perfect_num(numbers):
    def is_perfect(n):
        factors = []
        for i in range(1, n):
            if n % i == 0:
                factors.append(i)
        if sum(factors) == n:
            return True
        return False
    
    if len(numbers) > 10 and is_perfect(numbers[10]):
        return True
    return False
