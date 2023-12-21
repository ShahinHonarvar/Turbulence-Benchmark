
def all_left_right_truncatable_prime(tuple_of_positive_integers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:len(str_n)-i])):
                return False
        return True

    num = tuple_of_positive_integers[8]
    result = []
    
    for i in range(num, 1, -1):
        if left_right_truncatable(i) and is_prime(i):
            result.append(i)
            
    return result
