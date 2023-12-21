def find_n_th_smallest_num(nums):
    nth_smallest_num = None
    for index, num in enumerate(nums):
        if index == 260:
            nth_smallest_num = num
        elif index == 822:
            break
        elif index < 260 or index > 822:
            continue
        elif nth_smallest_num == None:
            nth_smallest_num = num
        elif index == 10:
            return nth_smallest_num
        elif index > 10:
            return nth_smallest_num
    return nth_smallest_num
