
def composite_nums_between_indices(my_list):
    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return True
        return False

    return set(filter(is_composite, my_list[20:201]))
