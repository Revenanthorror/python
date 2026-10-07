from collections import defaultdict

def main():
    try:
        raw_participants = input("Введите имена участников через пробел: ").strip()
        if not raw_participants:
            return
        participants = raw_participants.split()
        
        n = int(input("Введите количество трат: "))
        spent = defaultdict(int)
        for p in participants:
            spent[p] = 0
            
        print(f"Введите {n} трат (формат: Имя Сумма):")
        for _ in range(n):
            parts = input().split()
            name = parts[0]
            amount = int(parts[1])
            spent[name] += amount
    except (EOFError, ValueError):
        return

    total_spent = sum(spent.values())
    num_people = len(participants)
    fair_share = total_spent / num_people
    
    balances = {}
    for p in participants:
        balances[p] = round((spent[p] - fair_share) * 100)
        
    debtors = []
    creditors = []
    
    for p, bal in balances.items():
        if bal < 0:
            debtors.append([p, -bal])
        elif bal > 0:
            creditors.append([p, bal])
            
    transactions = []
    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor_name, debt_amt = debtors[i]
        creditor_name, cred_amt = creditors[j]
        
        transfer = min(debt_amt, cred_amt)
        transactions.append((debtor_name, creditor_name, transfer / 100.0))
        
        debtors[i][1] -= transfer
        creditors[j][1] -= transfer
        
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1
            
    print("\nМинимальные переводы:")
    print(len(transactions))
    for debtor, creditor, amt in transactions:
        print(f"{debtor} {creditor} {amt:.2f}")

if __name__ == "__main__":
    main()