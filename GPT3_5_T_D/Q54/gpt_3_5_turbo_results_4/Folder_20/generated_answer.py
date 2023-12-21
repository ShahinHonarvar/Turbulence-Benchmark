
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    result = []
    for number in range(x-1, 1, -1):
        if is_prime(number):
            num_str = str(number)
            is_right_truncatable = True
            for i in range(len(num_str)-1, 0, -1):
                if not is_prime(int(num_str[:i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                result.append(number)
    return sorted(result, reverse=True)
