
def if_perfect_num(lst):
    def is_perfect(n):
        divisors = [1]
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n / i:
                    divisors.append(n // i)
        return sum(divisors) == n

    return is_perfect(lst[23])
