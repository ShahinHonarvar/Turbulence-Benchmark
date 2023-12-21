
def find_n_th_smallest_num(numbers):
    sorted_nums = sorted(numbers[127:849])  # Sort the numbers in the required range
    return sorted_nums[9]  # Return the 10th smallest number from the sorted range
