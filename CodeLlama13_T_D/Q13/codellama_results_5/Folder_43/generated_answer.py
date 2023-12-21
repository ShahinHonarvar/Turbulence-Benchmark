
def find_second_largest_num(numbers):
    if len(numbers) <= 1:
        return None
    
    sorted_nums = sorted(numbers)[68:87]
    second_largest = sorted_nums[-2]
    return second_largest
