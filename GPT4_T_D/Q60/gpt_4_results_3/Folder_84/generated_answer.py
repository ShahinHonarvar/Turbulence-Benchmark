
def all_left_right_truncatable_prime(numbers):
    x = numbers[630]

    def check_prime(n):
        if n == 1: 
            return False
    
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0: 
                return False   
        return True

    def truncatable(n):
        str_n = str(n)
        for i in range(len(str_n)):
            if not check_prime(int(str_n[i:])) or not check_prime(int(str_n[:len(str_n) - i])):
                return False
        return True

    return sorted([n for n in range(10, x+1) if check_prime(n) and "0" not in str(n) and truncatable(n)], reverse=True)
