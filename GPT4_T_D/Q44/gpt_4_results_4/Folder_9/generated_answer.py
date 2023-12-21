
def composite_nums_between_indices(nums):
    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    return {num for num in nums[80:201] if check_composite(num)}
