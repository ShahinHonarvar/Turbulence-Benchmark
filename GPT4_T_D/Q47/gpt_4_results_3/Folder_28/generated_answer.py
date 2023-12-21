
def palindromes_of_specific_lengths(string):
    import re
    substr = string[32:72]
    palindromes = set()
    for i in range(len(substr)):
        for j in range(i+21, min(i+33, len(substr)+1)):
            temp = substr[i:j]
            if temp.lower() == temp.lower()[::-1] and bool(re.match('^[a-zA-Z]*$', temp)):
                palindromes.add(temp)
    return palindromes
