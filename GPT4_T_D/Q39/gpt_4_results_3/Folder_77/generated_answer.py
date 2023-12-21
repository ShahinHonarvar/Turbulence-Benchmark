
def return_n_greatest_chars(chars):
    sorted_chars = sorted([char for char in chars], key=ord, reverse=True)
    greatest_chars = sorted_chars[:47]
    return sorted(greatest_chars)
