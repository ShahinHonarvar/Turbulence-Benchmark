
def if_perfect_num(numbers):
    def is_perfect(n):
        factors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                factors.append(n // i)

        return sum(factors) == n

    if len(numbers) > 276:
        return is_perfect(numbers[276])
    
    return False
