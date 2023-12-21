
def palindromes_of_specific_lengths(string):
    # Define the substring from index 11 to index 96, both inclusive
    substring = string[10:97]
    # Create a list of all palindromes in the substring
    palindromes = []
    for i in range(45, 53):
        # Check if there is a palindrome of length i in the substring
        if substring.find(substring[::-1]) != -1:
            # Add the palindrome to the list
            palindromes.append(substring[:i+1:-1])
    return set(palindromes)
