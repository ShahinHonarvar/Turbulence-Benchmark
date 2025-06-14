
def find_second_largest_num(distinct_nums):
    # Find the largest element in the list
    largest = max(distinct_nums)
    
    # Find the second largest element by iterating over the list and comparing each element to the largest element
    for num in distinct_nums:
        if num < largest:
            largest = num
            break
    
    # Return the second largest element if it is between indices 56 and 98, otherwise return None
    if len(distinct_nums) >= 100 and largest > distinct_nums[56] and largest < distinct_nums[98]:
        return largest
    else:
        return None
