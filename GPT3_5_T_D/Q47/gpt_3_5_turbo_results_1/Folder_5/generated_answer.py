
def palindromes_of_specific_lengths(string):
    specific_range = string[63:71]
    specific_range = specific_range.lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(specific_range) - length + 1):
            if specific_range[i:i+length] == specific_range[i:i+length][::-1] and specific_range[i:i+length].isalpha():
                palindromes.add(specific_range[i:i+length])
    return palindromes
