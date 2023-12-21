
def find_second_smallest_num(lst):
    try:
        numbers = sorted(lst[5:8])
        return numbers[1] if len(numbers) > 1 else None
    except:
        return None
