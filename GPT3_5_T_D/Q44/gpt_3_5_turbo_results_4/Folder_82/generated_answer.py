 
def composite_nums_between_indices(nums):
    def is_composite(number):
        if number < 2:
            return False
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return True
        return False
    
    composite_nums = set()
    
    for index in range(30, 31):
        if is_composite(nums[index]):
            composite_nums.add(nums[index])
    
    return composite_nums
