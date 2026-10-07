def find_median(lst):
    n = len(lst)
    if n % 2 == 1:
        return float(lst[n // 2])
    else:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2.0

def main():
    try:
        n_str = input("Введите количество элементов N: ").strip()
        if not n_str:
            return
        n = int(n_str)
        
        print(f"Введите {n} чисел (через пробел или по одному в строке):")
        x = []
        while len(x) < n:
            x.extend(map(int, input().split()))
    except (EOFError, ValueError):
        return

    x_sorted = sorted(x)
    q2 = find_median(x_sorted)
    
    mid = n // 2
    if n % 2 == 1:
        lower_half = x_sorted[:mid]
        upper_half = x_sorted[mid+1:]
    else:
        lower_half = x_sorted[:mid]
        upper_half = x_sorted[mid:]
        
    q1 = find_median(lower_half)
    q3 = find_median(upper_half)
    
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    outliers_count = sum(1 for val in x if val < lower_bound or val > upper_bound)
    print("\nКоличество выбросов:", outliers_count)

if __name__ == "__main__":
    main()