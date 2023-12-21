
def all_left_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num > 10:
            if not is_prime(num):
                return False
            num = int(str(num)[1:])
        return is_prime(num)

    x = numbers[78]
    result = []
    for i in range(x-1, 1, -1):
        if is_left_truncatable_prime(i):
            result.append(i)
    return result
