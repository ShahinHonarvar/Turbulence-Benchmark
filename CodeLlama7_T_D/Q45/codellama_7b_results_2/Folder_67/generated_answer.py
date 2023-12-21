 def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length at least 5 in the given string
    for i in range(2, len(string) - 4):
        # Extract the current substring and its reverse
        substring = string[i:i+5]
        reversed_substring = substring[::-1]
        # Check if the substring is a palindrome by comparing it to its reverse
        if substring == reversed_substring:
            # If the substring is a palindrome, add it to the set of palindromes
            palindromes.add(substring)
    return palindromes
