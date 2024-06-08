"""Module providing performance measurement"""
import timeit

import matplotlib.pyplot as plt
import pandas as pd

from data_set import generate_random_data
from sort import insertion_sort, merge_sort

def merge_sort_wrapper(data):
    """Wrapper functions to use with timeit"""
    merge_sort(data.copy())

def insertion_sort_wrapper(data):
    """Wrapper functions to use with timeit"""
    insertion_sort(data.copy())

def timsort_wrapper(data):
    """Wrapper functions to use with timeit"""
    sorted(data)


small_data = generate_random_data(100)
medium_data = generate_random_data(1000)
large_data = generate_random_data(10000)

# Measure performance
small_data_merge = timeit.timeit(lambda: merge_sort_wrapper(small_data), number=10)
small_data_insertion = timeit.timeit(lambda: insertion_sort_wrapper(small_data), number=10)
small_data_timsort = timeit.timeit(lambda: timsort_wrapper(small_data), number=10)

medium_data_merge = timeit.timeit(lambda: merge_sort_wrapper(medium_data), number=10)
medium_data_insertion = timeit.timeit(lambda: insertion_sort_wrapper(medium_data), number=10)
medium_data_timsort = timeit.timeit(lambda: timsort_wrapper(medium_data), number=10)

large_data_merge = timeit.timeit(lambda: merge_sort_wrapper(large_data), number=10)
large_data_insertion = timeit.timeit(lambda: insertion_sort_wrapper(large_data), number=10)
large_data_timsort = timeit.timeit(lambda: timsort_wrapper(large_data), number=10)

results = {
    "Algorithm": ["Merge Sort", "Insertion Sort", "Timsort"] * 3,
    "Dataset Size": ["Small"] * 3 + ["Medium"] * 3 + ["Large"] * 3,
    "Time (s)": [
        small_data_merge, small_data_insertion, small_data_timsort,
        medium_data_merge, medium_data_insertion, medium_data_timsort,
        large_data_merge, large_data_insertion, large_data_timsort
    ]
}

def main():
    """Function displaying performance results"""
    # Display results
    df = pd.DataFrame(results)
    print(df)

    # Plotting the results
    fig, ax = plt.subplots()
    for key, grp in df.groupby(['Dataset Size']):
        ax = grp.plot(ax=ax, kind='line', x='Algorithm', y='Time (s)', label=key)

    plt.title('Sorting Algorithm Performance')
    plt.xlabel('Algorithm')
    plt.ylabel('Time (s)')
    plt.legend(title='Dataset Size')
    plt.show()

if __name__ == "__main__":
    main()
