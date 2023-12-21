
def find_second_largest_num(numbers):
    if len(numbers) < 49:
        return None

    nums = numbers[30:49]
    largest = max(nums)
    nums.remove(largest)
    second_largest = max(nums)
    
    return second_largest
