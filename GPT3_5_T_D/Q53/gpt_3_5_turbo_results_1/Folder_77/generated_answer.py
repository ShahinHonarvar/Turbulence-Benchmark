
def palindrome_of_length_at_least_n(string):
    string = string.lower()  
    palindromes = set()
  
    for i in range(len(string) - 148):
        for j in range(149, len(string) - i + 1):
            substring = string[i:i+j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
  
    return palindromes
