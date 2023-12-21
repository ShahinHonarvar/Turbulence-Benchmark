
def all_left_truncatable_prime(numbers):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def is_left_truncatable_prime(n):
        if '0' in str(n):
            return False
        return all(is_prime(int(str(n)[i:])) for i in range(len(str(n))))
      
    x = numbers[71]
    result = [i for i in range(2, x) if is_left_truncatable_prime(i)]
    result.sort(reverse=True)
    return result
