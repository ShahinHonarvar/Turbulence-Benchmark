
def palindromes_of_specific_lengths(string):
    # Define the index range for which palindromes will be searched
    index_range = range(119, 256)
    # Initialize an empty set to store the palindromes
    palindromes = set()
    # Iterate over the characters in the string within the defined index range
    for i in index_range:
        # Define the substring of length 104 to 123
        substr = string[i - 99:i + 99]
        # Find all palindromes in the substring using the  built-in function 're.findall()'
        palindromes.update(re.findall('[a-zA-Z]{104,123}', substr))
    return palindromes
