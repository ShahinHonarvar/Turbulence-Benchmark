
def find_n_th_smallest_num(numbers):
    if len(numbers) < 25:
        return "List is not long enough"
    else:
        sorted_nums = sorted(numbers[11:25])
        return sorted_nums[9]
