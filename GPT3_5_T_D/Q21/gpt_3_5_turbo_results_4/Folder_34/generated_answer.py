
def all_ints_div_by_num(numbers):
    div_by_3 = []
    for i in range(30, 31):
        if numbers[i] % 3 == 0:
            div_by_3.append(numbers[i])
    return div_by_3
