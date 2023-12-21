
def palindromes_of_specific_lengths(string):
    import re
    substring = string[10:56].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+3, min(i+8, len(substring)+1)):
            if re.match("^[a-z]*$", substring[i:j]):
                if substring[i:j]==substring[i:j][::-1]:
                    palindromes.add(substring[i:j])
    return palindromes
