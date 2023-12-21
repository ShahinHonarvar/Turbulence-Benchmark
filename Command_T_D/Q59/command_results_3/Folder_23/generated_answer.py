import re
def all_left_truncatable_prime(nums):
    # Your code here
    return [int(p) for p in re.findall(r'(2[89]7|3[579]9)', str(nums[77])))]
