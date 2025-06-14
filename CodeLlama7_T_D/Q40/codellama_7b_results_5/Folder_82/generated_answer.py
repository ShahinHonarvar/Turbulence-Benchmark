 def return_n_smallest_chars(s):
    # Create a list of tuples containing the ASCII value and character for each character in the input string
    chars = [(ord(c), c) for c in s]
    # Sort the list of tuples by the ASCII value in ascending order
    chars.sort()
    # Return the first 60 characters of the sorted list, since we want to return a list of exactly 60 characters
    return [c for _, c in chars[:60]]
