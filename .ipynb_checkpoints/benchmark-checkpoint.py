import random
import time
from sorts import selection_sort, bubble_sort, radix_sort_lsd

# Функция для генерации данных разных типов
def generate_data(n, kind, seed=0):
    rng = random.Random(seed)
    if kind == "random":
        return [rng.randint(0, 10**6) for _ in range(n)]
    if kind == "sorted":
        return list(range(n))
    if kind == "reversed":
        return list(range(n, 0, -1))
    if kind == "nearly_sorted":
        a = list(range(n))
        for _ in range(max(1, int(n * 0.05))):
            i, j = rng.randrange(n), rng.randrange(n)
            a[i], a[j] = a[j], a[i]
        return a
    if kind == "duplicates":
        return [rng.randint(1, 5) for _ in range(n)]
    raise ValueError(kind)

# Функция для замера времени
def benchmark(sort_fn, sizes, kinds, repeats=3):
    results = {}
    for kind in kinds:
        for n in sizes:
            times = []
            for r in range(repeats):
                data = generate_data(n, kind, seed=r)
                t0 = time.perf_counter()
                sort_fn(data)
                t1 = time.perf_counter()
                times.append(t1 - t0)
            mean_t = sum(times) / len(times)
            results[(kind, n)] = {"mean_time": mean_t}
    return results

print("Функции для замеров готовы!")