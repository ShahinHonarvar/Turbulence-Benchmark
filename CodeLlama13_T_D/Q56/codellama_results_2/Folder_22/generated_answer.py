
def all_substring_of_size_n(s):
    return [''.join(s[i:j]) for i in range(len(s)) for j in range(i+1, len(s)+1) if len(''.join(s[i:j])) == 22 and len(set(''.join(s[i:j]))) == 22]
