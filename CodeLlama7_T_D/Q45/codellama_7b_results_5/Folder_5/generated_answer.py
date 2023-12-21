
def palindromes_between_indices(string, start_index=4, end_index=8):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string
    for i in range(start_index, end_index + 1):
        # Get the substring that starts at index i and ends at index i
        substring = string[i:]
        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Add the substring to the set of palindromes
            palindromes.add(substring)
    # Return the set of palindromes
    return palindromes

def is_palindrome(string):
    # Check if the string is an empty string or a single-character string
    if len(string) <= 1:
        return True

# Check if the first and last characters of the string are the same
if string[0] == string[-1]:
    # Recursively check if the substring that starts at index 1 and ends at index -2 is a palindrome
    return is_palindrome(string[1:-1])
