
def palindrome_of_length_n(s):
    return set((y for y in (x for x in ((''.join(list(set(y[::-1])))) for y in re.findall('([A-Za-z]{60})', s))) if len(y) == 60 and not (''.join(list(set(y[::-1]))) in ['']))))
