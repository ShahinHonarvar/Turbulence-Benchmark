
def all_ints_not_div_by_num(numbers):
    result = []
    for num in numbers[:5]:
        if num % 13 != 0:
            result.append(num)
    return result
