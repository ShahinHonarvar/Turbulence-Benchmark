
def gcf_two_nums(lst):
    def gcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    if len(lst) < 84:
        return "List too short"
    else:
        return gcf(lst[83], lst[14])
