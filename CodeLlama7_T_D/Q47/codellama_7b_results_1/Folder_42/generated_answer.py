
def palindromes_of_specific_lengths(string, index_range=(43, 95), length_range=(18, 47)):
    # Convert the string to lowercase for case-insensitive comparison
    lowercase_string = string.lower()

    # Find all substrings in the specified range that are palindromes

    palindrome_substrings = []

    for i in range(*index_range):

        substring = lowercase_string[i:i+len(lowercase_string)]

        if substring == substring[::-1]:

            palindrome_substrings.append(substring)


    # Filter the palindromes to those with lengths between 18 and 47 (both inclusive)

    filtered_palindromes = [substring for substring in palindrome_substrings if length_range[0] <= len(substring) <= length_range[1]]

    return set(filtered_palindromes)
