
def composite_nums_between_indices(num_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return True
        return False

    composite_numbers = set()
    for i in range(75, 86):
        if i < len(num_list) and is_composite(num_list[i]):
            composite_numbers.add(num_list[i])
    return composite_numbers
