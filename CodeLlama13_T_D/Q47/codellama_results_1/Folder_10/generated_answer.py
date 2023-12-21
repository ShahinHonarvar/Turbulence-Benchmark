
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string that are between 16 and 39 characters long,
    # and occur within the substring from index 16 to index 60 (both inclusive).
    palindromes = set()
    for i in range(16, 61):
        for j in range(i+16, i+39+1):
            substr = string[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
