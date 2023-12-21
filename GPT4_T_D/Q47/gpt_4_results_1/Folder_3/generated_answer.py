
def palindromes_of_specific_lengths(string):
    substr = string[27:96]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+49, min(i+52,len(substr)+1)):
            temp = substr[i:j]
            if temp == temp[::-1]:
                if temp.isalpha():
                    palindromes.add(temp.lower())
    return palindromes
