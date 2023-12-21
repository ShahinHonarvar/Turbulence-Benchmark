
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[73]
    result = []
    for i in range(x-1, 1, -1):
        if is_prime(i):
            num = str(i)
            is_truncatable = True
            while len(num) > 0:
                if not is_prime(int(num)):
                    is_truncatable = False
                    break
                num = num[:-1]
            if is_truncatable:
                result.append(i)
    return sorted(result, reverse=True)
