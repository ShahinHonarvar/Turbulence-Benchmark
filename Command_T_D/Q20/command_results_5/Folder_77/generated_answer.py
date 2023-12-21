import heapq
def find_n_th_smallest_num(nums):
    q, heap = nums[:], heapq.heapify(nums[::-1])
    for i in range(len(q) - 1):
        heapq.heapreplace(heap, q[i])
    return heap[len(q) - 1 - 9]
