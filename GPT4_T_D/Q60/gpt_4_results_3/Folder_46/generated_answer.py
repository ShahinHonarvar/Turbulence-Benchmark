
def all_left_right_truncatable_prime(numbers):
    x = numbers[33]
    primes = [i for i in range(2, x+1) if all(i%j !=0 for j in range(2, int(i ** 0.5) + 1))]
    truncatable_primes = []
    
    def truncate(number):
        str_num = str(number)
        str_len = len(str_num)
        for i in range(str_len):
            if not is_prime(int(str_num[i:])):
                return False
            if not is_prime(int(str_num[:str_len - i])):
                return False
        return True

    def is_prime(num):
        for div in range(2, num):
            if num % div == 0:
                return False
        return True
    
    for prime in primes:
        if '0' not in str(prime) and truncate(prime):
            truncatable_primes.append(prime)

    return sorted(truncatable_primes)
