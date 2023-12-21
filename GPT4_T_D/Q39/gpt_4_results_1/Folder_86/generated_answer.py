
def return_n_greatest_chars(characters):
    if len(set(characters)) != len(characters):
        raise ValueError("All characters should be distinct")
    sorted_characters = sorted(characters, key=ord)
    return sorted_characters[-34:]
