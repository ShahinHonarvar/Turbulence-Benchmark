 def palindrome_of_length_at_least_n(string, n=3):
    # Remove any non-alphanumeric characters from the string
    cleaned_string = "".join(c for c in string if c.isalnum())
    # Create a set to store the palindromes
    palindromes = set()
    # Loop through each substring of length >= n in the cleaned string
    for i in range(len(cleaned_string) - n + 1):
        # Check if the current substring is a palindrome
        if cleaned_string[i:i+n] == cleaned_string[i:i+n][::-1]:
            # Add the palindrome to the set
            palindromes.add(cleaned_string[i:i+n])
    return palindromes
