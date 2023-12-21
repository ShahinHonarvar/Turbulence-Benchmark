
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[11]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        prime = True
        temp = str(num)
        while len(temp) > 1:
            if not is_prime(int(temp)):
                prime = False
                break
            temp = temp[1:-1]
        if prime:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)
