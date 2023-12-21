
def composite_nums_between_indices(lst):
    def check_composite(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
            else:
                return False
        else:
            return False

    return {i for i in lst[17:79] if check_composite(i)}
