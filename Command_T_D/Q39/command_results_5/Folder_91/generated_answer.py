import sys
def return_n_greatest_chars(s):
    max_list = [ch for ch in s]
    return [max(max_list[:6]) for max_list in zip(*sorted(zip(*max_list)))]
