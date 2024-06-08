"""Module providing a function merging lists."""
from heapq import heappush, heappop

def merge_k_lists(lists):
    """Function merging lists"""
    heap = []
    for i, sorted_list in enumerate(lists):
        if sorted_list:
            heappush(heap, (sorted_list[0], i, 0))

    merged_list = []
    while heap:
        val, list_idx, element_idx = heappop(heap)
        merged_list.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            heappush(heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1))

    return merged_list

if __name__ == "__main__":
    # Example usage
    lists_to_merge = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged = merge_k_lists(lists_to_merge)
    print("Відсортований список:", merged)
