
def composite_nums_between_indices(numbers_list):
    composite_nums = set()
    for number in numbers_list[75:86]:
        if number > 1 and any(number % i == 0 for i in range(2, number)):
            composite_nums.add(number)
    return composite_nums
