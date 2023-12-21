
def all_left_right_truncatable_prime(t):
    from itertools import product
    x = t[945]
    all_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def generate_left_right_truncatable_primes():
        result = []
        for i in range(2, 10):
            result += [i]
            for j in range(1, 21):
                temp = []
                for num in product(all_nums, repeat=j):
                    num = str(i) + ''.join(num)
                    if '0' not in num and is_prime(int(num)):
                        temp.append(int(num))
                result += temp
        return result
    
    truncatable_primes = list(filter(lambda x: is_prime(x) and is_prime(int(str(x)[1:])) and is_prime(int(str(x)[:-1])), generate_left_right_truncatable_primes()))

    if len(truncatable_primes) == 0: return truncatable_primes
    else: return [i for i in truncatable_primes if i <= x]
