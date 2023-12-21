
from itertools import permutations

def palindromes_between_indices(string):
    sub_string = string[3:9].lower()
    palindromes = set()
    
    for i in range(4, len(sub_string)+1):
        for p in permutations(sub_string, i):
            check_string = ''.join(p)
            if check_string == check_string[::-1]:
                palindromes.add(check_string)
                
    return palindromes
