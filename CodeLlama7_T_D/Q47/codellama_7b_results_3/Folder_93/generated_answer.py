
def palindromes_of_specific_lengths(string, index1=17, index2=95):
    # Find all substrings between indices 17 and 95 (inclusive)
    substrings = string[index1:index2+1]
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over each substring
    for substring in substrings:
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            # If it is, add it to the set of palindromes
            palindromes.add(substring)
    # Iterate over each length range and find the palindromes in that range
    for length_range in [(13, 49)]:
        for substring in substrings:
            if length_range[0] <= len(substring) <= length_range[1]:
                # Check if the substring is a palindrome
                if substring == substring[::-1]:
                    # If it is, add it to the set of palindromes
                    palindromes.add(substring)
    return palindromes
