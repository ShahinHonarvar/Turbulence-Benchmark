
def all_pos_ints_exclusive(numbers):
    result = []
    for i in range(67, 90):
        if i < len(numbers) and numbers[i] > 0:
            result.append(numbers[i])
    return result
