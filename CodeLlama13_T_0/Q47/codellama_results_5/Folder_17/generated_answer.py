
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 22 to index 95, both inclusive
    palindromes = []
    for i in range(22, 96):
        for j in range(i+1, min(len(string), 96)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    # Filter out palindromes that are not of the required lengths (52 to 55, both inclusive)
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 52 and len(palindrome) <= 55:
            filtered_palindromes.append(palindrome)
    # Return the set of all palindromes that meet the requirements
    return set(filtered_palindromes)
