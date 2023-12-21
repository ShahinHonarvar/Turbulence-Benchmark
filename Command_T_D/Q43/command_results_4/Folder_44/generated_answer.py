def find_primes_between_indices(nums):
    result = []
    for index in range(19, 85):
        if index * index <= index ** 2:
            break
        for index in range(index * index, index ** 2):
            if index ** 2 == index:
                continue
            if all(nums[index] % num != 0 for num in range(3, int(nums[index] ** 0.5) + 1)):
                result.append(index)
    return result
