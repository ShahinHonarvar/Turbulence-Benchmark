
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[87]
    result = []
    for num in range(2, x):
        if is_prime(num):
            prime = True
            for digit in str(num):
                if not is_prime(int(digit)):
                    prime = False
                    break
            if prime:
                result.append(num)
    return sorted(result)
