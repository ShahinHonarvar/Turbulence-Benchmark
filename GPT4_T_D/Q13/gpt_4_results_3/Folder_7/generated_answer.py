
def find_second_largest_num(numbers):
    if len(numbers) < 925:
        return None
    else:
        sublist = numbers[661:925]
        sublist.sort()
        return sublist[-2]
