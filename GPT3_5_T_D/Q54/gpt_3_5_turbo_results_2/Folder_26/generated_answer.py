
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[81]
    result = []

    for num in range(x - 1, 1, -1):
        temp = num
        if is_prime(temp):
            while temp > 9:
                temp //= 10
                if not is_prime(temp):
                    break
            else:
                result.append(num)

    return sorted(result, reverse=True)
