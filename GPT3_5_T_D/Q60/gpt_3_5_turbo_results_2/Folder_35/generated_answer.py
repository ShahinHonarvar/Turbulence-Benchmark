
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    truncatable_primes = []
    x = numbers[177]
    for number in range(2, x+1):
        if '0' not in str(number):
            truncated_number = str(number)
            while len(truncated_number) > 1:
                truncated_number = truncated_number[1:-1]
                if not is_prime(int(truncated_number)):
                    break
            else:
                truncatable_primes.append(number)
    return sorted(truncatable_primes)
