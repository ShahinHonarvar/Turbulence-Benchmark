
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[46]
    primes = []
    result = []

    for num in range(11, x+1):
        if '0' in str(num):
            continue
        
        truncatable = True
        prime = True
        
        while num > 0:
            if not is_prime(num):
                prime = False
                break
            num //= 10
        
        if prime:
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0

            while num > 0:
                if not is_prime(num):
                    prime = False
                    truncatable = False
                    break
                num = int(str(num)[:-1])

        if prime and truncatable:
            primes.append(num)

    primes.sort(reverse=True)
    return primes
