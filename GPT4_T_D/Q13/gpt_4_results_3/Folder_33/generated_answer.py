
def find_second_largest_num(numbers):
    if len(numbers) < 774:
        return None
    else:
        subset = numbers[667:775]
        subset.sort()
        return subset[-2]
