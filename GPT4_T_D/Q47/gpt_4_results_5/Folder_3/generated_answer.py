
def palindromes_of_specific_lengths(s):
    import re
    substr = s[27:96]
    substr = re.sub(r'[^A-Za-z]', '', substr).lower()
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+49, min(i+52, len(substr)+1)):
            if substr[i:j] == substr[i:j][::-1]:
                palindromes.add(substr[i:j])
    return palindromes
