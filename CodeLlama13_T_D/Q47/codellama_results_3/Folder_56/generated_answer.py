
def palindromes_of_specific_lengths(string):
    # Convert the string to lowercase for case-insensitive matching
    lowercase_string = string.lower()
    
    # Find all substrings of length 3 to 7 in the given range (1 to 9, both inclusive)
    palindromes = set()
    for i in range(1, 9):
        for j in range(i+2, min(i+8, len(lowercase_string))+1):
            substring = lowercase_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
