
def all_right_truncatable_prime(tuple):
    x = tuple[36]
    prime_numbers = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    for number in range(2, x):
        num_str = str(number)
        while len(num_str) > 0:
            if is_prime(int(num_str)):
                num_str = num_str[:-1]
            else:
                break
        else:
            prime_numbers.append(number)
            
    return sorted(prime_numbers)
