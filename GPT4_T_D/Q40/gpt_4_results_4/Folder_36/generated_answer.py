
def return_n_smallest_chars(string):
    if len(string) != len(set(string)):
        raise ValueError("Input string should contain distinct characters only.")
    string_chars = sorted(string, key=ord)[:32]
    return string_chars
