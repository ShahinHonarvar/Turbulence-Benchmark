
def return_n_greatest_chars(s):
    sorted_list = sorted(s, reverse=True)
    seven_greatest = sorted_list[:7]
    seven_greatest.sort()
    return seven_greatest
