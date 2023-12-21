
def composite_nums_between_indices(list_of_nums):
    def is_composite(n):
        if n < 2: 
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for i in range(10, min(101, len(list_of_nums))):
        if is_composite(list_of_nums[i]):
            composites.add(list_of_nums[i])
    return composites
