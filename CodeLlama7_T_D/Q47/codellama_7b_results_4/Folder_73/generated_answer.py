
def palindromes_of_specific_lengths(string):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(21, 63):
        substring = string[i:i+1]
        if substring == substring[::-1]:
            palindromes.append(substring)
    # Filter out palindromes that are not of the correct length
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 22 and len(palindrome) <= 33:
            filtered_palindromes.append(palindrome)
    # Return the set of filtered palindromes
    return set(filtered_palindromes)
