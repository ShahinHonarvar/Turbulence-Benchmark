
def return_n_smallest_chars(characters):
    if len(characters) != 68:
        return "Please provide a string with exactly 68 distinct characters"
    list_chars = list(characters)
    list_chars.sort(key=ord)
    list_chars.reverse()
    return list_chars
