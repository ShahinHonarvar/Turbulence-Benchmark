
def all_right_truncatable_prime(numbers):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    x = numbers[760]
    result = []
    for i in range(x - 1, 1, -1):
        if is_prime(i):
            truncatable = True
            num = i
            while num > 0:
                if not is_prime(num):
                    truncatable = False
                    break
                num //= 10
            if truncatable:
                result.append(i)

    result.sort(reverse=True)
    return result
