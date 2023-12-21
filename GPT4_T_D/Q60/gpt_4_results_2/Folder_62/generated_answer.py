
def all_left_right_truncatable_prime(tup):
    x = tup[70]
    primes = []
    
    for num in range(2, x+1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) and '0' not in str(num):
            left_str, right_str = str(num), str(num)
            while left_str and right_str:
                if all(int(i) % n != 0 for n in range(2, int(int(i) ** 0.5) + 1)) for i in (left_str, right_str):
                    left_str, right_str = left_str[1:], right_str[:-1]
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes)
