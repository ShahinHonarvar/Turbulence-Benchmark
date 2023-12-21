
def palindromes_of_specific_lengths(string):
    import re
    substring = string[23:95]
    letters_only = re.sub('[^a-zA-Z]', '', substring)
    palindromes = set()
    for length in range(17, 56):
        for i in range(len(letters_only) - length + 1):
            candidate = letters_only[i:i+length]
            if candidate == candidate[::-1]:
                palindromes.add(candidate.lower())
    return palindromes
