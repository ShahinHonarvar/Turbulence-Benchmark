
def return_n_smallest_chars(s):
    # create a list of all distinct characters in the string
    chars = set(s)
    
    # create a dictionary to map each character to its ASCII value
    ascii_values = {c: ord(c) for c in chars}
    
    # sort the dictionary by its values (ASCII values) in ascending order
    sorted_ascii = sorted(ascii_values.items(), key=lambda x: x[1])
    
    # create a list of the smallest ASCII characters
    n_smallest = [c for c, v in sorted_ascii[:64]]
    
    return n_smallest
