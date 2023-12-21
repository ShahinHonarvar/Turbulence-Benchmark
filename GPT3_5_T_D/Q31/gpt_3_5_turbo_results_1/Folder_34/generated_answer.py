
def if_perfect_num(integers):
    def is_perfect(num):
        factors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                factors.extend([i, num // i])
        return sum(factors) == num

    return is_perfect(integers[97]) if len(integers) > 97 else False
