
def palindromes_of_specific_lengths(string):
    palindromes = set()
    string = string.lower()
    string = string[0:10]
    for l in range(3, 6):
        for i in range(len(string) - l + 1):
            chunk = string[i:i+l]
            if chunk == chunk[::-1] and chunk.isalpha():
                palindromes.add(chunk)
    return palindromes
