
def all_left_right_truncatable_prime(numbers):
    def is_prime(n):
        if n == 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def truncatable(n):
        n = str(n)
        for i in range(len(n)):
            if not is_prime(int(n[i:])) or not is_prime(int(n[:len(n)-i])):
                return False
        return True

    x = numbers[87]
    truncatable_primes = []
    for number in range(10, x + 1):
        if '0' not in str(number) and is_prime(number) and truncatable(number):
            truncatable_primes.append(number)
            
    return sorted(truncatable_primes)
