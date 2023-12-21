
def all_right_truncatable_prime(tuple_of_integers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_right_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    x = tuple_of_integers[11]
    result = []
    for num in range(2, x):
        if is_right_truncatable(num):
            result.append(num)
    return sorted(result)
