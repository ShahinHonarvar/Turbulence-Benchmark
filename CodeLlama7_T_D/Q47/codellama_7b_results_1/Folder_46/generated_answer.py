
def palindromes_of_specific_lengths(string):
    # Define the substring range for searching palindromes
    substring_range = string[11:97]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each character in the substring range
    for i in range(len(substring_range)):
        # Define the current character and its index
        char = substring_range[i]
        index = i + 11
        # Check if the current character is a letter (not a space or punctuation)
        if char.isalpha():
            # Initialize an empty string to store the palindrome
            palindrome = ""
            # Iterate over each character in the substring range starting from the current index and ending at the end of the substring range
            for j in range(index, len(substring_range)):
                # Define the current character and its index
                char2 = substring_range[j]
                # Check if the current character is a letter (not a space or punctuation)
                if char2.isalpha():
                    # Add the current character to the palindrome string
                    palindrome += char2
            # Check if the palindrome has the required length between 29 to 62 (both inclusive)
            if len(palindrome) >= 29 and len(palindrome) <= 62:
                # Add the palindrome to the set of palindromes
                palindromes.add(palindrome)
    # Return the set of palindromes in a case-insensitive manner
    return {palindrome.lower() for palindrome in palindromes}
