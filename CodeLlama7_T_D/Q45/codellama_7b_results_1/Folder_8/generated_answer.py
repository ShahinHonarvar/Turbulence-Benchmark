
def palindromes_between_indices(string):
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Loop through each possible substring of length 5 in the given string
    for i in range(len(string) - 4):
        # Extract the substring and reverse it
        substring = string[i:i+5]
        reversed_substring = substring[::-1]
        # If the substring is a palindrome, add it to the set of palindromes
        if reversed_substring == substring:
            palindromes.add(substring)
    return palindromes
