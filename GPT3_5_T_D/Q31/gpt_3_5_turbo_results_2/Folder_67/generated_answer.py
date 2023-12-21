
def if_perfect_num(nums):
    def is_perfect(num):
        if num < 2:
            return False
        total = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                total += i
                if i != num // i:
                    total += num // i
        return total == num

    return is_perfect(nums[43])
