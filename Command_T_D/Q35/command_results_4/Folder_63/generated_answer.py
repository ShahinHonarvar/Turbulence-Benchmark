import itertools
def remove_repeat_chars(s):
    return ''.join(c for c in itertools.chain(s[:81], s[82:86], s[87:]))
