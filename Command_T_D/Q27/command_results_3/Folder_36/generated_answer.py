
import itertools

def insert_after_index(nums):
    return [x for x in list(itertools.chain.from_iterable(zip(nums[:360], nums[361:])) + [[699, 556]]))
