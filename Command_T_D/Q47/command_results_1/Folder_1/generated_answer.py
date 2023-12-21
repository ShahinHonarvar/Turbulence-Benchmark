def palindromes_of_specific_lengths(s):
    return set(filter(lambda x: (x in s[15:-15].lower() and len(x) in range(40, 73)), 'abcdefghijklmnopqrstuvwxyz'))
