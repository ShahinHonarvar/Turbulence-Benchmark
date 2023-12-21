
def all_substring_of_size_n(s):
    return [ss for ss in (s[i:j] for i in range(len(s)) for j in range(i+63, len(s)+1) if s[i:j] not in set(s[:i])) if len(set(ss)) == 63]
