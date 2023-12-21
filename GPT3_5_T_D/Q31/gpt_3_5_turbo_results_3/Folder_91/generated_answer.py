
def if_perfect_num(numbers):
    def is_perfect(n):
        factors = []
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return sum(factors) == n

    return is_perfect(numbers[6])
