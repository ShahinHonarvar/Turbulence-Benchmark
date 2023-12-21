
def gcf_two_nums(nums_list):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    return gcf(nums_list[18], nums_list[37])
