
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[18]
    prime_numbers = []
    for i in range(x-1, 0, -1):
        if '0' in str(i):
            continue
        is_truncatable = True
        for j in range(len(str(i))):
            if not is_prime(int(str(i)[j:])):
                is_truncatable = False
                break
        if is_truncatable:
            prime_numbers.append(i)
    return prime_numbers
