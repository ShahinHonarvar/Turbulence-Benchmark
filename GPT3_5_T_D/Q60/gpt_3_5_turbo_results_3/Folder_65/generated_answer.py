
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    result = []
    for x in numbers:
        if x >= 10:
            truncatable = True
            number = str(x)
            for i in range(len(number)):
                if number[i] == '0':
                    truncatable = False
                    break
                if not is_prime(int(number[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(x)
    return sorted(result)
