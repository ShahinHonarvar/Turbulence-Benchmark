
def palindromes_between_indices(string):
    from itertools import permutations

    string = string[1:8].lower()
    subset = set(string)
    palindromes = set()

    for ch in subset:
        temp_str = string.replace(ch, '', 2)
        single = ''
        if string.count(ch) % 2 != 0:
            single = ch

        string_list = sorted(list(temp_str))
        for item in permutations(string_list, len(string_list)//2):
            possible_palindrome = ''.join(item)\
                + single\
                + ''.join(reversed(item))
            if len(possible_palindrome) > 2 and possible_palindrome == possible_palindrome[::-1]:
                palindromes.add(possible_palindrome)

    return palindromes
