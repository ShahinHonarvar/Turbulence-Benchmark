
def return_nth_smallest_ascii(string):
    # Find the nth smallest ASCII value among the characters in the string
    nth = 9
    ascii_values = []
    for i in range(51, 79):
        char = string[i]
        if char not in ascii_values:
            ascii_values.append(ord(char))
    
    # Sort the list of ASCII values and return the nth element
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[nth-1])
