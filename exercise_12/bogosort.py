import random
import time

def is_sorted(arr):
    """
    Sprawdza, czy lista jest posortowana.
    """
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bogo_sort(arr):
    """
    Implementacja Bogo Sort.
    """
    while not is_sorted(arr):
        random.shuffle(arr)

def quick_sort(arr):
    """
    Implementacja QuickSort.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

def merge_sort(arr):
    """
    Implementacja MergeSort.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    """
    Pomocnicza funkcja do scalania dwóch list w MergeSort.
    """
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged

def insertion_sort(arr):
    """
    Implementacja Insertion Sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generowanie losowej listy
arr = random.sample(range(1, 200000), 20000)

# Porównanie czasów wykonania
start_time = time.time()
bogo_sort(arr.copy())
bogo_sort_time = time.time() - start_time

start_time = time.time()
quick_sort(arr.copy())
quick_sort_time = time.time() - start_time

start_time = time.time()
merge_sort(arr.copy())
merge_sort_time = time.time() - start_time

start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

# Wyświetlanie wyników
print("Czas wykonania Bogo Sort:", bogo_sort_time, "sekundy")
print("Czas wykonania QuickSort:", quick_sort_time, "sekundy")
print("Czas wykonania MergeSort:", merge_sort_time, "sekundy")
print("Czas wykonania Insertion Sort:", insertion_sort_time, "sekundy")
