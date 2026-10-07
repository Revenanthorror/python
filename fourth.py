import re
from collections import defaultdict
from datetime import datetime

def parse_line(line):
    line = line.strip()
    if not line:
        return None
    
    if ';' in line:
        parts = [p.strip() for p in line.split(';')]
    elif ',' in line:
        parts = [p.strip() for p in line.split(',')]
    else:
        parts = line.split()
        
    if ',' in line and len(parts) > 3:
        cost_str = parts[-2] + '.' + parts[-1]
        date_str = parts[0]
        pizza_str = ",".join(parts[1:-2])
    elif len(parts) == 3:
        date_str, pizza_str, cost_str = parts[0], parts[1], parts[2]
    else:
        return None
    
    pizza_str = pizza_str.replace('"', '').strip()
    
    cost_str = cost_str.replace(',', '.')
    try:
        cost = float(cost_str)
    except ValueError:
        return None
        
    date_str = date_str.replace('/', '.')
    date_parts = date_str.split('.')
    if len(date_parts) != 3:
        return None
    
    day, month, year = date_parts
    if len(day) == 1: day = '0' + day
    if len(month) == 1: month = '0' + month
    if len(year) == 2: year = '20' + year
    
    try:
        dt = datetime.strptime(f"{day}.{month}.{year}", "%d.%m.%Y")
        norm_date = dt.strftime("%d.%m.%Y")
    except ValueError:
        return None

    return norm_date, pizza_str, cost

def main(file_lines):
    pizza_counts = defaultdict(int)
    daily_totals = defaultdict(float)
    valid_orders = []
    
    for line in file_lines:
        parsed = parse_line(line)
        if parsed is None:
            continue
        
        date, pizza, cost = parsed
        pizza_counts[pizza] += 1
        daily_totals[date] += cost
        valid_orders.append((date, pizza, cost))
        
    if not valid_orders:
        return

    sorted_pizzas = sorted(pizza_counts.items(), key=lambda x: x[1], reverse=True)
    print("а)")
    for pizza, count in sorted_pizzas:
        print(f"{pizza} - {count}")
        
    sorted_dates = sorted(daily_totals.keys(), key=lambda d: datetime.strptime(d, "%d.%m.%Y"))
    print("\nб)")
    for date in sorted_dates:
        print(f"{date} {daily_totals[date]:.2f}".rstrip('0').rstrip('.'))
        
    max_order = max(valid_orders, key=lambda x: x[2])
    cost_fmt = f"{max_order[2]:.2f}".rstrip('0').rstrip('.')
    print("\nв)")
    print(f"{max_order[0]} {max_order[1]} {cost_fmt}")
    
    avg_cost = sum(o[2] for o in valid_orders) / len(valid_orders)
    print("\nг)")
    print(f"{avg_cost:.2f}")

sample_input = """28.02.2026 Пепперони 420
28.02.2026 Гавайская 440
01.03.2026 Пепперони 430.50
01.03.2026 Четыре сыра 399.99
02.03.2026 Пепперони 400
27.02.2026;Четыре сыра;388,80
28.02.2026 "Четыре сыра" 399,99
20/02/2026,Баварская,440.00
424242 аааа уф
21.02.2026,Гавайская,399.90
03.03.2026 "Баварская" 480
01.04.2026,Акция! Все по 99,99,99,99
28/02/2026 Пепперони 435""".splitlines()

if __name__ == "__main__":
    main(sample_input)