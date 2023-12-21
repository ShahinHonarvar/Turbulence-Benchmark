
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = numbers[54]
    result = []

    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = str(num)
            truncatable = True
            while truncatable and len(temp) > 1:
                temp = temp[:-1]
                if not is_prime(int(temp)):
                    truncatable = False

            if truncatable:
                result.append(num)

    return sorted(result, reverse=True)
