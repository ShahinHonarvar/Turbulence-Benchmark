
def palindromes_of_specific_lengths(string):
    # Define the index range for the substring
    start_index = 0
    end_index = 300
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each character in the string within the index range
    for i in range(start_index, end_index + 1):
        # Define the substring of length 50 to 60 starting from the current index
        substring = string[i:i + 60]
        # Check if the substring is a palindrome
        if is_palindrome(substring):
            # Add the palindrome to the set
            palindromes.add(substring)
    return palindromes

def is_palindrome(string):
    # Convert the string to lowercase for case-insensitive comparison
    lowercase_string = string.lower()
    # Check if the string is a palindrome by comparing it with its reverse
    return lowercase_string == lowercase_string[::-1]
