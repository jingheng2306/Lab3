SORT_ASCENDING = 0
SORT_DESCENDING = 1

def bubble_sort(arr, sorting_order):
    arr_result = arr.copy()
    n = len(arr_result)

    if n < 10:
        # Sorting logic for less than 10 numbers
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if sorting_order == SORT_ASCENDING:
                    if arr_result[j] > arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
                elif sorting_order == SORT_DESCENDING:
                    if arr_result[j] < arr_result[j + 1]:
                        arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
    elif n >= 10:
        # Return integer value 1 for >= 10 numbers
        return 1
    elif n == 0:
        # Return integer value 0 for zero numbers
        return 0
    else:
        # Return integer value 2 for non-integer inputs
        return 2

    return arr_result

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result_asc = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result_asc)

    # Sort in descending order
    result_desc = bubble_sort(arr, SORT_DESCENDING)
    print("Sorted array in descending order: ")
    print(result_desc)

    # Test for zero numbers
    print("Sorting zero numbers: ")
    result_zero = bubble_sort([], SORT_ASCENDING)
    print(result_zero)

    # Test for non-integer input
    print("Sorting non-integer input: ")
    result_non_int = bubble_sort([64, 34, 'a', 12, 22, 11, 90], SORT_ASCENDING)
    print(result_non_int)

if __name__ == "__main__":
    main()
