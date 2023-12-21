 def palindromes_of_specific_lengths(string, index_range=(45, 98), palindrome_lengths=(40, 47)):
    # Convert the input string to lowercase for case-insensitive comparison
    string = string.lower()

    # Define a lambda function to check if a substring is a palindrome

    is_palindrome = lambda substr: substr == substr[::-1]

    # Initialize an empty set to store the palindromes

    palindromes = set()

    # Iterate over the characters in the input string within the specified index range

    for i in range(*index_range):
        # Check if the current character is a palindrome

        if is_palindrome(string[i]):
            # If it is, add it to the set of palindromes

            palindromes.add(string[i])

    # Iterate over the palindromes in the set and check if they have the specified lengths

    for palindrome in palindromes:
        # Check if the length of the current palindrome is within the specified range

        if len(palindrome) in palindrome_lengths:
            # If it is, return the set of palindromes that meet the criteria

            return palindromes

    # If no palindromes with the specified lengths are found within the specified index range, return an empty set

    return set()
