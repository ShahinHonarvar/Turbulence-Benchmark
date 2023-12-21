
def all_left_truncatable_prime(tup):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))
    
    def is_left_truncatable(num):
        number = str(num)
        if '0' in number: 
            return False
        return all(is_prime(int(number[i:])) for i in range(len(number)))

    limit = tup[61]
    
    return sorted([i for i in range(1, limit) if is_prime(i) and is_left_truncatable(i)])
