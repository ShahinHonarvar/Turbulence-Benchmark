
def palindrome_of_length_n(string):
    # Remove non-alphanumeric characters from the string
    cleaned_string = "".join(c for c in string if c.isalnum())
    # Create a list of all substrings of the specified length
    substring_list = [cleaned_string[i:i+474] for i in range(len(cleaned_string)-473)]
    # Filter out any substrings that are not palindromes
    palindrome_list = [substring for substring in substring_list if substring == substring[::-1]]
    return set(palindrome_list)
