
def all_right_truncatable_prime(nums):
    x = nums[0]
    right_primes = []
    for num in range(2, x):
        str_num = str(num)
        for i in range(len(str_num)):
            sub_num = int(str_num[:len(str_num)-i])
            if all(sub_num % n != 0 for n in range(2, sub_num)):
                if i == len(str_num) - 1:
                    right_primes.append(num)
            else:
                break
    return sorted(right_primes, reverse=True)
