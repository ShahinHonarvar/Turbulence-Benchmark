
def all_even_ints_exclusive(nums):
    evens = []
    for num in nums[:5]:
        if num % 2 == 0:
            evens.append(num)
    return evens
