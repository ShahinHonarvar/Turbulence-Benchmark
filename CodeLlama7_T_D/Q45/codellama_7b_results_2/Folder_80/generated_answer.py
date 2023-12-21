
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible combination of letters in the given string
    for i in range(3, len(string)):
        # Check if the substring starting at index i and ending at index i + 7 is a palindrome
        if is_palindrome(string[i:i+7], True):
            # Add the palindrome to the set
            palindromes.add(string[i:i+7])
    # Return the set of palindromes
    return palindromes

def is_palindrome(string, case_insensitive=False):
    # If the string is empty or has only one character, it cannot be a palindrome
    if len(string) <= 1:
        return False

    # Check if the first and last characters of the string are equal
    if (case_insensitive and string[0].lower() == string[-1].lower()) or (not case_insensitive and string[0] == string[-1])):
        # If the first and last characters are equal, check if the substring starting at index 1 and ending at index len(string) - 2 is a palindrome
        return is_palindrome(string[1:-2], case_insensitive)
    else:
        # If the first and last characters are not equal, return False
        return False
