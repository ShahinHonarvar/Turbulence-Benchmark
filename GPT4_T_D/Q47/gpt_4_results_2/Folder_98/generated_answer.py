
def palindromes_of_specific_lengths(s):
    palindromes = set()
    string = s[:21].lower()

    for i in range(len(string)):
        for j in range(i+1, len(string)+1):
            substring = string[i:j]
            if substring == substring[::-1] and 5<=len(substring)<=80 and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
