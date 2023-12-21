
def return_nth_smallest_ascii(string):
    # Create a list of the ASCII values of all characters in the string
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    # Find the 11th smallest ASCII value among the characters between indices 25 to 45, both inclusive
    sorted_ascii_values = sorted(ascii_values)
    smallest_ascii_value = sorted_ascii_values[0]
    largest_ascii_value = sorted_ascii_values[-1]
    nth_smallest_ascii_value = 0

    for i in range(25, 46):
        if ascii_values[i] == smallest_ascii_value:
            nth_smallest_ascii_value = ascii_values[i]
            break

    return chr(nth_smallest_ascii_value)
