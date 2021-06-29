def insertionSort(unsorted_array):
    """Sort list of comparable elements into ascending order."""
    for k in range(len(unsorted_array)):
        curr = unsorted_array[k]
        j = k
        while j > 0 and unsorted_array[j - 1] > curr:
            unsorted_array[j] = unsorted_array[j - 1]
            j -= 1
        unsorted_array[j] = curr


a = [5, 4, 7, 3, 1]
insertionSort(a)
print(a)
