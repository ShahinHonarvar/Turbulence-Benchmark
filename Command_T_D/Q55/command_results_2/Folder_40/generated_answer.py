import functools
def lists_with_product_equal_n(nums):
    # If there are no numbers, return an empty list
    if not nums:
        return []
    # If there is only one number, return a list containing only that number
    if len(nums) == 1:
        return [[nums]]
    # If there are two numbers, return a list containing only that pair
    if len(nums) == 2:
        return [[nums]]
    # If there are more than two numbers, return a list containing only the pairs
    pairs = []
    # We start from the first two numbers in the list
    pair = [[nums[0], nums[1]]
    # We take every other number in the list
    for i in range(2, len(nums) - 1, 2):
        # We add the current number to the pair
        pair.append([nums[i]])
        # We remove the last number in the pair
        del pair[-2]
    # We add the last number to the pair
    pair.append([nums[-1]])
    # We create the list of pairs
    pairs.append(pair)
    # We return the list of pairs
    return pairs
