
def if_contains_anagrams(my_list):
    return len([i for i in my_list if ''.join(sorted(i)) in map(''.join, [[j for j in my_list if ''.join(sorted(j)) == ''.join(sorted(i))]][1:])]) <= 21
