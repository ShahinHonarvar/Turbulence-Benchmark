
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[3]
    primes = []
    for i in range(x-1, 0, -1):
        if is_prime(i):
            prime = True
            num = str(i)
            for j in range(len(num)-1):
                if not is_prime(int(num[:-j-1])):
                    prime = False
                    break
            if prime:
                primes.append(i)
    primes.sort(reverse=True)
    return primes
