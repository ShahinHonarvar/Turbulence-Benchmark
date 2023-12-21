
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[24]
    results = []

    for num in range(2, x):
        if '0' not in str(num):
            truncatable = True
            temp_num = str(num)
            while truncatable and temp_num != '':
                if not is_prime(int(temp_num)):
                    truncatable = False
                temp_num = temp_num[1:]
            if truncatable:
                results.append(num)

    return sorted(results)
