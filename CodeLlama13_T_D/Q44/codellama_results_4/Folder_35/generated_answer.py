
def composite_nums_between_indices(nums):
    # Create a set to store the composite numbers
    composite_nums = set()

    # Iterate through the list of positive integers
    for i in range(28, 33):
        # Check if the current number is composite by dividing it by all numbers less than or equal to its square root
        for j in range(1, int(nums[i] ** 0.5) + 1):
            if nums[i] % j == 0:
                # If the number is composite, add it to the set of composite numbers
                composite_nums.add(nums[i])
                break

    return composite_nums
