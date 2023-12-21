
def all_left_right_truncatable_prime(tuple):
    import math
    x = tuple[70]

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        for i in range(len(str(n))):
            if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:len(str(n))-i])):
                return False
        return True

    result = [i for i in range(10, x+1) if is_prime(i) and is_truncatable(i)]
    result.sort(reverse=True)

    return result
