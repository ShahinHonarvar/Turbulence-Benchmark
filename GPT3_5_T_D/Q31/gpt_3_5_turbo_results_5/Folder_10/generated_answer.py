
def if_perfect_num(numbers):
    def is_perfect_number(n):
        if n <= 1:
            return False
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == n
    
    return is_perfect_number(numbers[54])
