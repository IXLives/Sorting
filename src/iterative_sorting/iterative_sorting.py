# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        if smallest_index != i:
            swapped = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = swapped
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        swapped = False
        for j in range(i + 1, len(arr)):
            next_index = j
            x = arr[cur_index]
            y = arr[next_index]
            if arr[i] > arr[j]:
                arr[cur_index] = y
                arr[next_index] = x
                swapped = True
        if swapped == False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
