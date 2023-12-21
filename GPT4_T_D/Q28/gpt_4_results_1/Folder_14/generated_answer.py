
def return_nth_smallest_ascii(arg):
    subset_arg = arg[46:83]
    sorted_subset = sorted(subset_arg)
    if len(sorted_subset) >= 16:
        return sorted_subset[15]
    else:
        return "There are less than 16 characters between indices 46 and 82."
