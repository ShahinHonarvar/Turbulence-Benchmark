
def return_n_smallest_chars(string):
    chars = set(string)
    sorted_chars = sorted([(char, ord(char)) for char in chars], key=lambda x: x[1])
    return [char for char, value in sorted_chars[:28]]
