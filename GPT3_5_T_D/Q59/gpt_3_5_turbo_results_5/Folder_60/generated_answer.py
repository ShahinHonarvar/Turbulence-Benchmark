 
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(nums):
    x = nums[87]
    result = []

    def check_prime(num):
        if num < x and is_prime(num):
            result.append(num)
            for i in range(1, 10):
                new_num = int(str(num) + str(i))
                check_prime(new_num)

    for i in range(1, 10):
        check_prime(i)

    return sorted(result)
