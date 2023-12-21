
def palindromes_of_specific_lengths(string):
    # Define the substring range to consider
    substr = string[17:72]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the substring
    for i in range(len(substr)):
        # Define the starting index of the current palindrome
        start_index = i

        # Define the ending index of the current palindrome
        end_index = len(substr) - i - 1

        # Define the current palindrome as a substring of the original string
        current_palindrome = substr[start_index:end_index+1]

        # Check if the current palindrome meets the requirements
        if (len(current_palindrome) >= 50 and len(current_palindrome) <= 51) and current_palindrome.islower():
            # Add the current palindrome to the set of palindromes
            palindromes.add(current_palindrome)

    # Return the set of palindromes that meet the requirements
    return palindromes
