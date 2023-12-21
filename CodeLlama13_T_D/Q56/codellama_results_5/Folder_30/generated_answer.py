
def all_substring_of_size_n(s):
    return [''.join(s[i:i+79]) for i in range(len(s)-78) if not ''.join(s[i:i+79]).isdigit() and not ''.join(s[i:i+79]).startswith(' ') and not ''.join(s[i:i+79]).endswith(' ') and not any(x.isspace() for x in s[i:i+79])]
