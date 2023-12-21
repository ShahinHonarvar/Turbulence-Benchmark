
def gcf_two_nums(integer_list):
    def gcf(a, b):
        while(b):
            a, b = b, a % b
        return a

    return gcf(integer_list[20], integer_list[83])
