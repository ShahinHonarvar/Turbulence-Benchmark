
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[92]
    result = []
    for i in range(2, x):
        is_truncatable_prime = True
        if '0' not in str(i):
            for j in range(len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    is_truncatable_prime = False
                    break
            if is_truncatable_prime:
                result.append(i)
    return sorted(result)
