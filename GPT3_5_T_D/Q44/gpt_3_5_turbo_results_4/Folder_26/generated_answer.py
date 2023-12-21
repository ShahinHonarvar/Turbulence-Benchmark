
def composite_nums_between_indices(nums):
    start = 22
    end = 50
    composites = set()

    for i in range(start, end + 1):
        num = nums[i]
        if num < 4:
            continue
        for j in range(2, int(num**0.5) + 1):
            if num % j == 0:
                composites.add(num)
                break

    return composites
