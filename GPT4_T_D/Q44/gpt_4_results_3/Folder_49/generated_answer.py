
def composite_nums_between_indices(int_list):
    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composites = set()
    for index in range(90, 201):
        if index < len(int_list) and is_composite(int_list[index]):
            composites.add(int_list[index])
    return composites
