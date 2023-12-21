
def return_n_smallest_chars(chars):
    if len(chars) != 46:
        return 'Error: Length of string must be exactly 46 characters!'
    selected_chars = sorted([char for char in chars], key=ord)
    return selected_chars[::-1]
