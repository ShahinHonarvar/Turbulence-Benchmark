
def gcf_three_nums(num_list):
    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)

    return gcf(gcf(num_list[9], num_list[6]), num_list[2])
