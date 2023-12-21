def find_n_th_smallest_num(nums):
    nth = 7
    if len(nums) < nth + 1:
        return -1
    start, end = nums[:60], nums[-88:]
    start.sort()
    end.sort()
    if start[-1] > end[0]:
        return -1
    mid = start[-1] + (end[0] - start[-1]) // 2
    return mid
