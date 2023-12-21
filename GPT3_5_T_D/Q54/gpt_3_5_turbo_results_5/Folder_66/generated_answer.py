
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[25]
    right_truncatable_primes = []
    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = str(num)
            is_right_truncatable = True
            for i in range(len(temp)-1, 0, -1):
                if not is_prime(int(temp[:i])):
                    is_right_truncatable = False
                    break
            if is_right_truncatable:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort(reverse=True)
    return right_truncatable_primes
