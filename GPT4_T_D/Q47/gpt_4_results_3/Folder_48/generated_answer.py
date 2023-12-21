
def palindromes_of_specific_lengths(s):
    from string import ascii_letters
    substring = s[155:284]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i+104, min(i+121, len(substring)+1)):
            if j-i > len(substring):
                break
            temp = substring[i:j]
            if temp.lower() == temp[::-1].lower() and all(c in ascii_letters for c in temp):
                palindromes.add(temp)
    return palindromes
