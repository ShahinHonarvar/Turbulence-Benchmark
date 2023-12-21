import re
def all_even_ints_exclusive(nums):
    even = [x for x in range(276, 376) if nums[x] % 2 == 0]
    return [nums[i] for i in even if i in range( 276, 376 ) ]
