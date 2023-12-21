from typing import List


def composite_nums_between_indices(l: List[int]) -> set[int]:
    result = set()
    sliced_l = l[56:98 + 1]
    for i in sliced_l:
        if i < 4:
            continue
        for j in range(2, i):
            if i % j == 0:
                result.add(i)
                break
    return result
