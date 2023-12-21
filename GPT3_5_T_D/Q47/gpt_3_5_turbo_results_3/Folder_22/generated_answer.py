
import re

def palindromes_of_specific_lengths(string):
    substring = string[100:201].lower()
    palindromes = set()
    for i in range(len(substring)-4):
        for j in range(5, 11):
            if i+j <= len(substring):
                temp = substring[i:i+j]
                if temp.isalpha() and temp == temp[::-1]:
                    palindromes.add(temp)
    return palindromes
