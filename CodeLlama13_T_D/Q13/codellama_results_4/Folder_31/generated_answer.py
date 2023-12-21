
def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    
    sorted_nums = sorted(numbers)[75:89]
    second_largest = sorted_nums[-2]
    return second_largest
