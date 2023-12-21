
def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    else:
        sublist = numbers[64:67]
        sublist.sort()
        return sublist[1]
