
def composite_nums_between_indices(num_list):
    composites = set()
    for num in num_list[1:9]:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    composites.add(num)
                    break
    return composites
