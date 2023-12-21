
import sys

def insert_after_index(L):
    L.insert(L.index(905) + 1, 742)
    return L + [sys.maxsize]
