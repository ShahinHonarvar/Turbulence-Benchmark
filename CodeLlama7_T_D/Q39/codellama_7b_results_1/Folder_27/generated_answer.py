
def return_n_greatest_chars(string, n):
    # Check if the input string is valid
    if not string or len(string) == 0:
        raise ValueError("Invalid input string")

    # Check if the number of characters to return is valid
    if n <= 0 or n > len(string):
        raise ValueError("Invalid value for 'n'")

    # Sort the string in ascending order based on ASCII values
    sorted_string = "".join(sorted(string, key=lambda x: ord(x))))

    # Return the top 82 characters of the sorted string
    return "".join(sorted_string[:n])
