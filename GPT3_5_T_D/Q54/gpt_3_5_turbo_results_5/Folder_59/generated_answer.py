
def all_right_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    x = numbers[84]
    result = []

    for num in range(x-1, 1, -1):
        if is_prime(num):
            truncate = str(num)
            while truncate:
                if not is_prime(int(truncate)):
                    break
                truncate = truncate[:-1]
            else:
                result.append(num)

    return sorted(result, reverse=True)
