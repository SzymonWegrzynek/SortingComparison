from array_sortings.insertion_sort import insertion_sort
from array_sortings.python_sort import python_sort
from array_sortings.bubble_sort import bubble_sort
from array_sortings.merge_sort import merge_sort
from array_sortings.quick_sort import quick_sort
# from array_sortings.tim_sort import tim_sort
from prettytable import PrettyTable
import random
import time


def messure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)  
    end_time = time.time()
    return round(end_time - start_time, 3)


def generate_data(size):
    return [random.randint(1, 1000) for _ in range(size)]


def run_tests():
    sizes = [100, 1000, 10000]
    
    sorting_algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Python Sort": python_sort,
        "Quick Sort": quick_sort,
        # "Tim Sort": tim_sort,
    }

    table = PrettyTable()
    table.field_names = ["Algorithm", "Size", "Time"]

    for size in sizes:
        arr = generate_data(size)  
        for sort_name, sort_func in sorting_algorithms.items():
            time_taken = messure_time(sort_func, arr)  
            table.add_row([sort_name, size, time_taken])

    print(table)

run_tests()
