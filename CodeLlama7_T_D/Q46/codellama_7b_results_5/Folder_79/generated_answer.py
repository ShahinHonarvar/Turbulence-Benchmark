
def gcf_three_nums(my_list):
    # Calculate the greatest common factor of three numbers using the Euclidean algorithm
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Get the elements at indices 16, 87 and 95
    nums = [my_list[i] for i in [16, 87, 95]]
    # Calculate the greatest common factor of these three numbers
    return gcf(nums[0], nums[1]), gcf(nums[1], nums[2]), gcf(nums[2], nums[0])
