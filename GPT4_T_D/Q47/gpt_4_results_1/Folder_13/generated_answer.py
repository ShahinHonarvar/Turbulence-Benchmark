
def palindromes_of_specific_lengths(string):
    palindrome_set = set()
    substring = string[13:96]
    for i in range(len(substring)):
        for j in range(i + 57, min(i + 61, len(substring) + 1)):
            chunk = substring[i:j]
            if chunk.lower() == chunk[::-1].lower() and chunk.isalpha():
                palindrome_set.add(chunk)
    return palindrome_set
