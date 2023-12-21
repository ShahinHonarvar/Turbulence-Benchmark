
def all_left_right_truncatable_prime(numbers):
    from itertools import permutations
    x = numbers[177]
    primes = [2,3,5,7]
    not_primes = set()
    
    def is_prime(n):
        if n == 1: 
            return 0
        for i in primes: 
            if n % i==0:
                return 0
        else:
            primes.append(n)
            return 1
        
    def left_right_truncatable(num):
        number=str(num)
        for i in range(1,len(number)):
            if not (is_prime(int(number[i:])) and is_prime(int(number[:len(number)-i]))):
                return False 
        return True
    
    for num in permutations('123456789', len(str(x))):
        num = int(''.join(num))
        if num > x:
            continue
        if num not in not_primes:
            if is_prime(num):
                if left_right_truncatable(num):
                    not_primes.add(int(''.join(num)))
    return sorted(list(not_primes))
