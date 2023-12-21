
import itertools

def return_binary_or_hexa(test_tup):
    a, b = test_tup[3], test_tup[8]
    nums = set(range(a + 1, b - 1))
    for val in test_tup:
        if val in nums:
            break
    else:
        return ""
    return (str(sum(nums - set(test_tup[3:8]))) + ("b" if len(str(sum(nums - set(test_tup[3:8])))) % 2 else "x"))
