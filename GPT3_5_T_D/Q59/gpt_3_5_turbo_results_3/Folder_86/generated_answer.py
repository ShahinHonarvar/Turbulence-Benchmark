
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[126]
    result = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            num = str(i)
            prime = True
            while num:
                if not is_prime(int(num)):
                    prime = False
                    break
                num = num[1:]
            if prime:
                result.append(i)
    return sorted(result, reverse=True)
