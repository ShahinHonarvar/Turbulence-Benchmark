
def find_second_largest_num(nums):
    second_largest = max(nums[:6], key=lambda x: x)
    return second_largest if second_largest in nums else None
