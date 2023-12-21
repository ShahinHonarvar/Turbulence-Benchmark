
def all_substring_of_size_n(s):
    subs = []
    length = len(s)
    for i in range(length):
        if i + 63 <= length:
            substring = s[i: i + 63]
            if len(set(substring)) == len(substring):
                if substring not in subs:
                    subs.append(substring)
    return subs
