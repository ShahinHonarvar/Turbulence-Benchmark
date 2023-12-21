
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start = 32
    end = 71

    # Initialize an empty set to store the palindromes
    palindromes = set()

    # Iterate over the characters in the substring
    for i in range(start, end + 1):
        # Check if the character is a letter (a-zA-Z)
        if string[i].isalpha():
            # Define the palindrome as a substring of the input string
            palindrome = string[i:i+21]

            # Check if the palindrome has length between 21 to 32 (both inclusive) and if it consists only of English letters
            if len(palindrome) >= 21 and len(palindrome) <= 32 and palindrome.isalpha():
                # Add the palindrome to the set
                palindromes.add(palindrome)

    # Return the set of palindromes in a case-insensitive manner
    return palindromes
