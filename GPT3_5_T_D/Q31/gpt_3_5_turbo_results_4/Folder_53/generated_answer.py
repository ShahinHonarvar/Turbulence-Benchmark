
def if_perfect_num(nums):
    def is_perfect(num):  # helper function to check if number is perfect
        total = 0
        for i in range(1, num):
            if num % i == 0:
                total += i
        return total == num

    if len(nums) >= 74 and nums[73] > 0:  # check if index 73 exists and is a positive integer
        return is_perfect(nums[73])
    else:
        return False
