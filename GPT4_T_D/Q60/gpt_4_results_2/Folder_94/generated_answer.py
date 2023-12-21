
def all_left_right_truncatable_prime(numbers):
    def is_prime(num):
        if num <= 1 or (num % 2 == 0 and num > 2): 
            return False
        return all(num % i for i in range(3, int(num**0.5) + 1, 2))
    
    def is_truncatable(num):
        if '0' in str(num):
            return False
        for i in range(1, len(str(num))):
            if not(is_prime(int(str(num)[i:])) and is_prime(int(str(num)[:i]))):
                return False
        return True

    x = numbers[43]
    valid_num = []
    for n in range(2, x+1):
        if is_prime(n) and is_truncatable(n):
            valid_num.append(n)
    return sorted(valid_num)
