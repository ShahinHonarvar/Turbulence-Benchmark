
def find_second_smallest_num(numbers):
    index_range = numbers[:5]
    if len(index_range) < 2:
        return None
    else: 
        index_range.sort()
        return index_range[1]
