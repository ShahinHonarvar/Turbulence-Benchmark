
def all_right_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[10]
    result = []

    for num in range(x-1, 1, -1):
        if is_prime(num):
            temp = str(num)
            flag = True
            while temp != '':
                if not is_prime(int(temp)):
                    flag = False
                    break
                temp = temp[:-1]
            if flag:
                result.append(num)

    return sorted(result, reverse=True)
