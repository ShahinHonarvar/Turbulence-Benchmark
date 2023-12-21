
def return_n_greatest_chars(s: str) -> List[str]:
    # Create a dictionary with the character as key and its ASCII value as value
    char_to_ascii = {c: ord(c) for c in s}
    # Sort the dictionary by its values in descending order
    sorted_dict = sorted(char_to_ascii.items(), key=lambda x: x[1], reverse=True)
    # Return the top 29 characters from the sorted dictionary
    return [c for c, _ in sorted_dict[:29]]
