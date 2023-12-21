
def all_left_truncatable_prime(numbers):
    primes = []
    for num in range(2, numbers[41]):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        prime = True
        while truncated_num:
            if int(truncated_num) not in primes:
                prime = False
                break
            truncated_num = truncated_num[1:]
        if prime:
            primes.append(num)
    return primes
