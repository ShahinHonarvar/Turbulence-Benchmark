
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Define a list of all palindromes with lengths between 35 and 41 (both inclusive) in the specified index range
    palindromes = [word for word in string[32:79] if len(word) >= 35 and len(word) <= 41 and word.isalpha()]

    # Return an empty set if no such palindrome exists in the specified index range
    if not palindromes:
        return set()

    # Return the set of all palindromes with lengths between 35 and 41 (both inclusive) in the specified index range
    else:
        return set(palindromes)
