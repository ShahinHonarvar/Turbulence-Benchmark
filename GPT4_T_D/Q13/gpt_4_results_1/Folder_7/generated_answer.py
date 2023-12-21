
def find_second_largest_num(numbers):
    if len(numbers) < 924:
        return None
    else:
        sorted_nums = sorted(numbers[661:925], reverse=True)
        if len(sorted_nums) < 2:
            return None
        else:
            return sorted_nums[1]
