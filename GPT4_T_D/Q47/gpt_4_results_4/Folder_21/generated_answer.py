
def palindromes_of_specific_lengths(s):
    substr = s[100:296]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+136, min(i+161, len(substr)+1)):
            temp = substr[i:j]
            if temp == temp[::-1] and temp.isalpha():
                palindromes.add(temp.lower())
    return palindromes
