 def palindromes_of_specific_lengths(string, index_range=(40, 94), lengths=(45, 51)):
    # Remove characters outside of the specified index range
    string = string[index_range[0]:index_range[1]]
    # Initialize an empty set to store palindromes
    palindromes = set()
    # Loop through each length in the specified range

    for length in lengths:
        # Find all substrings of the specified length

        substrings = [string[i:i+length] for i in range(len(string)-length+1)]
        # Check if any of the substrings are palindromes

        for substring in substrings:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
