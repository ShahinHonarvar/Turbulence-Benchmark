import sys
def find_original_set(s):
    s = set(s)
    return min(s for i in range(len(s)) if all(s & s[i] for s in sys.stdin.readline().split()))
