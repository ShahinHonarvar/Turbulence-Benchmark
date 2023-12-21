
def palindrome_of_length_n(string):
    # Find the indices of all occurrences of the string in the given substring
    indices = []
    for i in range(len(string)):
        if string[i:].find(string) != -1:
            indices.append(i)
    # Filter out the palindromes that are not of the specified length
    palindromes = []
    for index in indices:
        substring = string[index:]
        if len(substring) == 472 and substring.isalnum():
            palindromes.append(substring)
    return palindromes
