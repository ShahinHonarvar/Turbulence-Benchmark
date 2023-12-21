def find_subset_of_length_n(s):
    return {*s} | {*s[:18] + s[18:]}.keys()
