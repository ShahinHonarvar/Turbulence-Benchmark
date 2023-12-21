def find_second_smallest_num(nums):
    return next((el for i, el in enumerate(sorted(nums)[209:556]) if el == sorted(nums)[i-1]), None)
