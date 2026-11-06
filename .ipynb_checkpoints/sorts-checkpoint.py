def selection_sort(arr: list[int | float]) -> tuple[list[int | float], int, int]:
    """
    Сортировка выбором (Selection Sort).
    
    Сложность:
        - По времени: O(N^2) во всех случаях (best, average, worst).
        - По памяти: O(1) (in-place, дополнительная память не требуется).
        
    Возвращает: (отсортированный массив, число сравнений, число перестановок).
    """
    a = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return a, comparisons, swaps


def bubble_sort(arr: list[int | float]) -> tuple[list[int | float], int, int]:
    """
    Пузырьковая сортировка с флагом (Bubble Sort).
    
    Сложность:
        - По времени: O(N^2) в худшем и среднем случаях, O(N) в лучшем (на отсортированных данных).
        - По памяти: O(1) (in-place).
        
    Возвращает: (отсортированный массив, число сравнений, число перестановок).
    """
    a = arr.copy()
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return a, comparisons, swaps


def radix_sort_lsd(arr: list[int | float]) -> tuple[list[int | float], int, int]:
    """
    Поразрядная сортировка LSD (Radix Sort).
    
    Сложность:
        - По времени: O(d * (N + k)), где d - число разрядов, k - основание (10).
        - По памяти: O(N + k) для хранения корзин (buckets).
        
    Возвращает: (отсортированный массив, число сравнений, число записей).
    """
    a = arr.copy()
    comparisons = 0
    writes = 0
    if not a:
        return a, comparisons, writes
    
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for x in a:
            digit = (int(x) // exp) % 10  # int(x) на случай float
            buckets[digit].append(x)
            writes += 1
        a = [x for bucket in buckets for x in bucket]
        writes += len(a)
        exp *= 10
    return a, comparisons, writes