
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[14]
    primes = []
    for num in range(2, x+1):
        if '0' not in str(num):
            truncated_num = str(num)
            while len(truncated_num) > 1 and is_prime(int(truncated_num)):
                truncated_num = truncated_num[1:len(truncated_num)-1]
            if len(truncated_num) == 1 and is_prime(int(truncated_num)):
                primes.append(num)
    primes.sort(reverse=True)
    return primes
