
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            number_str = str(number)
            if '0' not in number_str:
                is_truncatable = True
                while len(number_str) >= 1:
                    if not is_prime(int(number_str)):
                        is_truncatable = False
                        break
                    number_str = number_str[1:]
                if is_truncatable:
                    primes.append(number)
    return sorted(primes, reverse=True)
