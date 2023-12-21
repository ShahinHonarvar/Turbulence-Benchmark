
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    x = numbers[22]
    for num in range(x - 1, 0, -1):
        if '0' not in str(num):
            n = num
            while n > 0:
                if not is_prime(n):
                    break
                n //= 10
            else:
                result.append(num)
    return result
