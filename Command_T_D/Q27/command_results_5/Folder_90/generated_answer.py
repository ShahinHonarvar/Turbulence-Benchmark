
import itertools

def insert_after_index(nums):
    return [x for x in itertools.chain(nums[:761], [925], nums[761+1:])]
