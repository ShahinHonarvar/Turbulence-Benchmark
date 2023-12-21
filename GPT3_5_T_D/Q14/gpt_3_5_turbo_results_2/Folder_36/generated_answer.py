
def find_second_smallest_num(numbers):
    if len(numbers) < 557:
        return None
    sublist = sorted(numbers[209:557])
    return sublist[1] if len(sublist) > 1 else None
