from collections import Counter
## не смог короче через get получить список, через файл сделал, надо просто рядом поместить mbox.txt и все
def main(file_path="mbox.txt"):
    authors = []
    
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if line.startswith("From "):
                parts = line.split()
                if len(parts) > 1:
                    authors.append(parts[1])
                    
    if not authors:
        print("Отправители не найдены или файл пуст.")
        return

    counts = Counter(authors)
    most_common_author, max_count = counts.most_common(1)[0]

    print("Список всех найденных адресов отправителей (уникальные):")
    for email in sorted(set(authors)):
        print(email)

    print("\n" + "="*40)
    print(f"Самый активный отправитель: {most_common_author}")
    print(f"Количество отправленных писем: {max_count}")

if __name__ == "__main__":
    main("mbox.txt")