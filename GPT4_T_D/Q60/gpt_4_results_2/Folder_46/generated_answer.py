
def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    primes = []
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
  
    def is_truncatable(n):
        strn = str(n)
        if '0' in strn: return False
        for i in range(len(strn)):
            if not is_prime(int(strn[i:])) or not is_prime(int(strn[:len(strn)-i])):
                return False
        return True

    for i in range(10, x+1):
        if is_prime(i):
            if is_truncatable(i):
                primes.append(i)
    return sorted(primes)
