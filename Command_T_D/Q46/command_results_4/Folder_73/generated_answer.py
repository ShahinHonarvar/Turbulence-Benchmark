
def gcf_three_nums(nums):
    gcf = 1
    for i in range(1, max(nums) + 1):
        if all(num % i == 0 for num in nums):
            gcf = i
            break
    return gcf
