
def all_left_truncatable_prime(numbers):
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    x = numbers[31]
    result = []
    for i in range(10, x):
        if is_prime(i):
            truncatable = True
            number = str(i)
            for j in range(len(number)):
                if not is_prime(int(number[j:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(i)
    return sorted(result, reverse=True)
