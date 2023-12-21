
def find_second_smallest_num(numbers):
    numsInRange = numbers[66:78]
    if len(set(numsInRange)) < 2:
        return None
    sortedNums = sorted(set(numsInRange))
    return sortedNums[1]
