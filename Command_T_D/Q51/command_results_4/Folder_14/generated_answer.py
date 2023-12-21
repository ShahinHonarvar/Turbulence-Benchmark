import collections
import re
    anagrams['A' + chr(i+ord('a'))].add('a' + chr(i+ord('A')))
    for c in range(26):
        for d in range(26):
            anagrams['A' + chr(c+ord('a'))].add('a' + chr(d+ord('A')))
    for c in range(26):
        for d in range(26):
            for e in range(26):
                anagrams['A' + chr(c+ord('a'))].add('a' + chr(d+ord('A')) + chr(e+ord('a')))
    for c in range(26):
        for d in range(26):
            for e in range(26):
                for f in range(26):
                    anagrams['A' + chr(c+ord('a'))].add('a' + chr(d+ord('A')) + chr(e+ord('a')) + chr(f+ord('a')))
def if_contains_anagrams(s):
    if len(s) == 1:
        return False
    elif len(s) == 2:
        if len(s[0]) != len(s[1]):
            return False
        elif s[0] == s[1]:
            return True
        else:
            return False
    elif len(s) == 3:
        if len(s[0]) != len(s[1]) != len(s[2]):
            return False
        elif s[0] == s[1] == s[2]:
            return True
        elif s[0] == s[1]:
            return False
        elif s[1] == s[2]:
            return False
        else:
            return False
    elif len(s) == 4:
        if len(s[0]) != len(s[1]) != len(s[2]) != len(s[3]):
            return False
        elif s[0] == s[1] == s[2] == s[3]:
            return True
        elif s[0] == s[1] == s[3]:
            return False
        elif s[1] == s[2] == s[3]:
            return False
        elif s[0] == s[2] == s[3]:
            return False
        else:
            return False
    else:
        return False
