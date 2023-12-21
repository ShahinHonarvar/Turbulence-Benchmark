
def gcf_three_nums(nums):
    def get_gcf(a, b):
        while b:
            a, b = b, a % b
        return a
    
    indices = [21, 69, 41]
    elements = [nums[i] for i in indices]
    gcf = elements[0]
    for element in elements[1:]:
        gcf = get_gcf(gcf, element)
    return gcf
