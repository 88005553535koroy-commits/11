with open('продукты.txt', encoding='utf-8') as f:
    lines = f.readlines()
    print('Нужно купить:')
    total = 0
    for line in lines:
        parts = line.strip().split(',')
        amount = int(parts[1])
        price = int(parts[2])
        total += price * amount
        print(f"{parts[0]} - {amount} шт. за {price} руб.")
    print('Итоговая сумма: ', total, 'руб.')