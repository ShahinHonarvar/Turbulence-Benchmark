import sys
def find_original_set(X):
    return set.intersection(*[set(map(int, sys.stdin.readline().split())) for _ in range(746)])
