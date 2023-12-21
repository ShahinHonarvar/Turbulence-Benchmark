
def if_perfect_num(numbers):
    def is_perfect(n):
        if n <= 1:
            return False
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == n
    
    if len(numbers) > 41:
        return is_perfect(numbers[41])
    else:
        return False
