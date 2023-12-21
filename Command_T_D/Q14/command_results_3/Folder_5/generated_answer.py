def find_second_smallest_num(nums):
    secondSmallestNum = None
    for index, num in enumerate(nums):
        if index == 3:
            secondSmallestNum = num
        elif index == 4:
            secondSmallestNum = num
        elif index == 5:
            secondSmallestNum = num
        else:
            break
    return secondSmallestNum
