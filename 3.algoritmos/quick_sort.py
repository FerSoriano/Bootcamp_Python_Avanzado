
nums = [1, 5, 9, 2, 7, 6, 3, 8, 4, 0]


def quickSort(arr) -> list:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print("Pivot: ", pivot, "quickSort: ", left, "middle: ", mid, "quickSort: ", right) # noqa
    return quickSort(left) + mid + quickSort(right)


print("Lista original: ", nums)
print("Lista ordenada: ", quickSort(nums))

# TODO: Reviar la variante de QuickSort in place
