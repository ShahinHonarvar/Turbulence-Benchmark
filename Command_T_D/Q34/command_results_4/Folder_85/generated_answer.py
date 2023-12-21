import sys
import heapq
def find_original_set(x):
    s = set()
    for i in range(len(x)):
        s |= x[i]
    return s
def main():
    x = [find_original_set(s) for s in sys.stdin.read().split('\n')]
    heapq.heapify(x)
    while True:
        i = heapq.heappop(x)
        if i == None:
            break
        else:
            sys.stdout.write(str(i))
    main()
