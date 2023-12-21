
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[22]
    result = []
    for i in range(x-1, 1, -1):
        if '0' not in str(i):
            prime = True
            j = 10 ** len(str(i))
            while j > 1:
                j //= 10
                if not is_prime(i % j):
                    prime = False
                    break
            if prime:
                result.append(i)
    return sorted(result, reverse=True)
