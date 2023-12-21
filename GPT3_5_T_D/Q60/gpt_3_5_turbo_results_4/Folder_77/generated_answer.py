
def all_left_right_truncatable_prime(numbers):
    def is_truncatable_prime(n):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        if n < 10:
            return n in primes
        else:
            str_n = str(n)
            return int(str_n[0]) in primes and int(str_n[-1]) in primes and is_truncatable_prime(int(str_n[1:-1]))
    
    x = numbers[767]
    result = []
    for num in range(2, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return sorted(result, reverse=True)
