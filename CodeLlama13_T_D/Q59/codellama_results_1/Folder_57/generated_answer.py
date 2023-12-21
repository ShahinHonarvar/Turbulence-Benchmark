
def all_left_truncatable_prime(numbers):
    result = []
    for number in numbers:
        if is_left_truncatable_prime(number):
            result.append(number)
    return sorted(result, reverse=True)

def is_left_truncatable_prime(number):
    if not is_prime(number):
        return False
    for i in range(1, len(str(number))):
        if not is_prime(int(str(number)[i:] + str(number)[:-i])):
            return False
    return True

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
