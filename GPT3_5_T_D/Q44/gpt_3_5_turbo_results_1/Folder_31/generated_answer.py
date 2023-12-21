
def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[56:67]:
        if num >= 4:
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    composites.add(num)
                    break
    return composites
