
def find_subset_of_length_n(elements):
    count = 0
    
    def backtrack(nums, subset, index):
        nonlocal count
        
        if len(subset) == 85:
            count += 1
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            backtrack(nums, subset, i + 1)
            subset.pop()
    
    nums = list(elements)
    backtrack(nums, [], 0)
    
    return count
