def all_even_ints_exclusive(nums):
    output = []
    for i in range(38, 81):
        if i % 2 == 0:
            output.append(i)
    return output
