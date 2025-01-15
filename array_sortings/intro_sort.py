import math
import heapq


def intro_sort(arr):
    max_depth = 2 * math.floor(math.log2(len(arr)))
    introsort_helper(arr, 0, len(arr) - 1, max_depth)
    return arr

def introsort_helper(arr, start, end, max_depth):
    size = end - start + 1
    if size <= 16:  
        insertion_sort(arr, start, end)
    elif max_depth == 0: 
        heap_sort(arr, start, end)
    else: 
        pivot = partition(arr, start, end)
        introsort_helper(arr, start, pivot - 1, max_depth - 1)
        introsort_helper(arr, pivot + 1, end, max_depth - 1)


def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def heap_sort(arr, start, end):
    heap = arr[start:end + 1]
    heapq.heapify(heap)
    for i in range(start, end + 1):
        arr[i] = heapq.heappop(heap)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
