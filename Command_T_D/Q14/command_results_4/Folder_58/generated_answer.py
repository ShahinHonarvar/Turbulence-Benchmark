def find_second_smallest_num(lst):
    result = lst[min(len(lst), 310):min(len(lst), 370) + 1]
    return result[1] if result and len(result) > 1 else None
