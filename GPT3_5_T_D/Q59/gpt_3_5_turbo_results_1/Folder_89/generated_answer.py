
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = []
    
    for num in nums:
        if num < 10:
            continue

        num_str = str(num)
        prime = True
        
        for i in range(1, len(num_str)):
            truncated_num = int(num_str[i:])
            
            if truncated_num == 0 or not is_prime(truncated_num):
                prime = False
                break
        
        if prime:
            primes.append(num)

    primes.sort(reverse=True)
    return primes
