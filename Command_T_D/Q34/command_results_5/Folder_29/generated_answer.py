import sys
def find_original_set(s):
    return {k: v for k, v in sorted(s.items(), key=lambda i: i[1])}
