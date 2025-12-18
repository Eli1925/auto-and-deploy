from datetime import datetime

import random
import pandas as pd
import os

CATEGORIES = ['Бытовая химия', 'Текстиль', 'Кухонная утварь', 'Посуда', 'Средства для уборки', 'Хранение']

ITEMS = {
    'Бытовая химия': ['Средство для мытья посуды', 'Стиральный порошок', 'Ополаскиватель для белья', 'Средство для чистки сантехники', 'Многоцелевой очиститель', 'Средство от жира'],
    'Текстиль': ['Постельное бельё', 'Полотенце', 'Плед', 'Подушка', 'Коврик', 'Шторы'],
    'Кухонная утварь': ['Сковорода', 'Кастрюля', 'Кухонный нож', 'Разделочная доска', 'Силиконовая лопатка', 'Мерный стакан'],
    'Посуда': ['Обеденная тарелка', 'Чашка', 'Стакан', 'Салатник', 'Сервировочное блюдо', 'Кофейная пара'],
    'Средства для уборки': ['Швабра', 'Ведро', 'Губки для посуды', 'Щётка', 'Резиновые перчатки', 'Набор для уборки ковров'],
    'Хранение': ['Пластиковый контейнер', 'Органайзер для ящиков', 'Корзина для белья', 'Контейнер для круп', 'Вакуумный пакет', 'Настенный крючок']
}

def main():
    if datetime.today().weekday() == 6:
        return
    
    n_shops=3
    n_registers_per_shop=2
    n_receipts_per_register=10

    os.makedirs('data', exist_ok=True)

    for shop_num in range(1, n_shops + 1):
        for cash_num in range(1, n_registers_per_shop + 1):
            data = []
            
            for receipt in range(n_receipts_per_register):
                doc_id = f"R{shop_num}_{cash_num}_{receipt + 1}_{random.randint(1000, 9999)}"
                
                n_items_in_receipt = random.randint(1, 4)
                
                for _ in range(n_items_in_receipt):
                    category = random.choice(CATEGORIES)
                    
                    item = random.choice(ITEMS[category])
                    
                    amount = random.randint(1, 11)
                    price = round(random.uniform(30, 1200), 2)
                    
                    discount = round(random.uniform(0, price * 0.4), 2) if random.random() < 0.35 else 0.0
                    
                    data.append({
                        'doc_id': doc_id,
                        'item': item,
                        'category': category,
                        'amount': amount,
                        'price': price,
                        'discount': discount
                    })
            
            df = pd.DataFrame(data)
            
            filename = f"{shop_num}_{cash_num}.csv"
            filepath = os.path.join('data', filename)
            df.to_csv(filepath, index=False)
           
           

main()
