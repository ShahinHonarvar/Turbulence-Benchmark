
def composite_nums_between_indices(num_list):
    def check_composite(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
            else:
                return False
        else:
            return False
    return {num for i,num in enumerate(num_list[14:65]) if check_composite(num)}
