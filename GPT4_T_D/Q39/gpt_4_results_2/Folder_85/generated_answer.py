
def return_n_greatest_chars(char_string):
    if len(char_string) < 85:
        raise ValueError("The input string should contain at least 85 distinct characters")

    sorted_string = sorted(char_string, key=ord, reverse=True)
    return sorted_string[:85]
