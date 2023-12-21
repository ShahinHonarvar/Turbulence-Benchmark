
def all_left_right_truncatable_prime(nums):
    x = nums[89]
    primes = []
    for num in range(2, x+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)) and '0' not in str(num):
            str_num = str(num)
            left_right_truncatable = True
            for i in range(len(str_num)):
                if not all(int(str_num[j:i+1])%k!=0 for k in range(2, int(int(str_num[j:i+1])**0.5)+1)):
                    left_right_truncatable = False
                    break
            if left_right_truncatable:
                primes.append(num)
    return sorted(primes, reverse=True)
