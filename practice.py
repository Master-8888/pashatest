bread = input('Сколько буханок хлеба вы хотите: >>').strip()
bread_quantity = int(bread)
bread_price = 24.35
total_price = bread_price * bread_quantity

butter = input('Сколько масла вы хотите, г: >>').strip()
butter_quantity = float(butter)
butter_price_kg = 320.16
butter_price_g = butter_price_kg / 1000
total_butter_price = butter_price_g * butter_quantity

total = total_price + total_butter_price
total = round(total, 2)
print('*' * 50)
print('ФИСКАЛЬНЫЙ ЧЕК')
print(f'Общая сумма покупки: {total}')
print('=' * 50)