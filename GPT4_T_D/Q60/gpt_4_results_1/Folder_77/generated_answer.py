
def all_left_right_truncatable_prime(numbers):
    x = numbers[767]
    primes = []
    for number in range(11, x+1):

        if str(number).count('0') > 0:
            continue

        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5)+1):
                if n % i == 0:
                    return False
            return True
        
        if not is_prime(number):
            continue
            
        str_num = str(number)
        is_truncatable = True
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])) or not is_prime(int(str_num[:i])):
                is_truncatable = False
                break
            
        if is_truncatable:
            primes.append(number)
            
    return sorted(primes, reverse=True)
