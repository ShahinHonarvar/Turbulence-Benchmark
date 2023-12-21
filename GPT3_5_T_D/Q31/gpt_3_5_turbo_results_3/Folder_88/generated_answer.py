
def if_perfect_num(numbers):
    def get_divisors(n):
        divisors = []
        for i in range(1, n):
            if n % i == 0:
                divisors.append(i)
        return divisors

    def is_perfect_num(n):
        divisors = get_divisors(n)
        if sum(divisors) == n:
            return True
        return False

    return is_perfect_num(numbers[46])
