
import sys
input = sys.stdin.readline

def insert_at_index(lst):
    lst += [369]
    return lst[:983] + lst[983:1084] + lst[1084:]
