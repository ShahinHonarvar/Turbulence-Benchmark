
def gcf_two_nums(nums):
    def find_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    index_1 = 78
    index_2 = 16
    
    num_1 = nums[index_1]
    num_2 = nums[index_2]
    
    return find_gcf(num_1, num_2)
