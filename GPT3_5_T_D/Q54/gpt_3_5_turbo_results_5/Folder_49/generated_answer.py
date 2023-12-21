
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[14]
    result = []

    for num in range(2, x):
        if is_prime(num):
            right_truncatable = True
            temp = num // 10

            while temp > 0:
                if not is_prime(temp):
                    right_truncatable = False
                    break
                temp = temp // 10

            if right_truncatable:
                result.append(num)

    return sorted(result)
