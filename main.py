from array_sortings.insertion_sort import insertion_sort
from array_sortings.python_sort import python_sort
from array_sortings.bubble_sort import bubble_sort
from array_sortings.merge_sort import merge_sort
from array_sortings.quick_sort import quick_sort
from array_sortings.tim_sort import tim_sort
from array_sortings.intro_sort import intro_sort
# from prettytable import PrettyTable
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
        "Tim Sort": tim_sort,
        "Intro Sort": intro_sort
    }

    # table = PrettyTable()
    # table.field_names = ["Algorithm", "Size", "Time"]

    # for size in sizes:
    #     arr = generate_data(size)  
    #     for sort_name, sort_func in sorting_algorithms.items():
    #         time_taken = messure_time(sort_func, arr)  
    #         table.add_row([sort_name, size, time_taken])

    # print(table)

    print("Rozmiar danych | " + " | ".join(sorting_algorithms.keys()))
    print("-" * 115)

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]
        results = []
        for _, func in sorting_algorithms.items():
            test_data = data.copy()
            time_taken = messure_time(func, test_data)
            results.append(f"{time_taken:.3f} s")
        print(f"{size:<14} | " + " | ".join(results))

run_tests()
