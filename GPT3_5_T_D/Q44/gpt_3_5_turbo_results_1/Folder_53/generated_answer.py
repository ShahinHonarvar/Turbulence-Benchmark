
def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[222:223]:
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    composites.add(num)
                    break
    return composites
