
def palindromes_of_specific_lengths(string):
    substring = string[12:57]
    palindromes = set()
    for i in range(len(substring)-19):
        sub_substring = substring[i:i+20]
        if sub_substring.isalpha() and sub_substring.lower() == sub_substring.lower()[::-1]:
            palindromes.add(sub_substring)
    return palindromes
