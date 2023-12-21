
def find_second_largest_num(numbers):
    if len(numbers) < 80:
        return None

    sublist = numbers[29:80]
    sublist.sort(reverse=True)

    if len(sublist) == 1:
        return sublist[0]
    else:
        return sublist[1]
