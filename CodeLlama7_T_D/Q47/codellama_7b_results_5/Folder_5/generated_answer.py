
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive comparison
    string = string.lower()

    # Find the starting and ending indices of the substring in question
    start_index = 63
    end_index = 70

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate through each character in the substring
    for i in range(start_index, end_index + 1):

        # Check if the current character is a letter (i.e., not a space or other non-letter character)
        if string[i].isalpha():

            # Initialize an empty string to store the current palindrome
            palindrome = ""

            # Iterate through each character in the substring, starting from the current index and moving backwards
            for j in range(i, end_index + 1):

                # Add the current character to the palindrome string
                palindrome += string[j]

            # Check if the palindrome is of the correct length (between 4 and 5 characters)
            if len(palindrome) >= 4 and len(palindrome) <= 5:

                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)

    # Return the set of palindromes
    return palindromes
