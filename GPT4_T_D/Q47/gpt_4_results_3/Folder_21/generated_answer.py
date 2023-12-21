
def palindromes_of_specific_lengths(s):
    string = s[100:296]
    string = ''.join(e for e in string if e.isalnum())
    possible_palindromes = set()
    for i in range(len(string)):
        for j in range(i + 136, min(i + 161, len(string) + 1)):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower():
                possible_palindromes.add(substring)
    return possible_palindromes
