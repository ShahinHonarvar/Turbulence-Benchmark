
def composite_nums_between_indices(num_list):
    composite_nums = set()
    
    def check_composite(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return True
            else:
                return False
        else:
            return False

    for i in range(66,94):
        if i<len(num_list) and check_composite(num_list[i]):
            composite_nums.add(num_list[i])
    return composite_nums
