
def return_n_greatest_chars(s):
    # Create a dictionary of characters and their ASCII values
    char_ascii = {c: ord(c) for c in set(s)}

    # Sort the dictionary by value (ASCII value) in descending order
    sorted_char_ascii = sorted(char_ascii.items(), key=lambda x: x[1], reverse=True)

    # Create a list of the top 31 characters with the greatest ASCII values
    top_chars = [c for c, _ in sorted_char_ascii[:31]]

    return top_chars
