
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[77]
    prime_numbers = []
    for num in range(2, x):
        if '0' not in str(num):
            is_truncatable = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])):
                    is_truncatable = False
                    break
            if is_truncatable:
                prime_numbers.append(num)
    return sorted(prime_numbers)
