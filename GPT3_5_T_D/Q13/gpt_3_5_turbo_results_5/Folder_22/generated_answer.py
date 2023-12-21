
def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    else:
        sublist = numbers[40:201]
        sublist.sort(reverse=True)
        if len(sublist) > 1:
            return sublist[1]
        else:
            return None
