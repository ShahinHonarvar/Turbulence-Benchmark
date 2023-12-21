
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[46]
    right_truncatable_primes = []
    for number in range(x - 1, 1, -1):
        if is_prime(number):
            temp = str(number)
            while temp:
                if not is_prime(int(temp)):
                    break
                temp = temp[:-1]
            else:
                right_truncatable_primes.append(number)
    return sorted(right_truncatable_primes, reverse=True)
