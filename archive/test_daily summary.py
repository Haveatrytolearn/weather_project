from weather import generate_daily_summary, load_data_from_csv

# Загрузить данные из CSV
data = load_data_from_csv('tests/data/example_one.csv')

print("Загруженные данные:")
print(data)
print("\n" + "="*60 + "\n")

# Вызвать функцию
result = generate_daily_summary(data)

print("Результат generate_daily_summary():")
print(result)

print("\n" + "="*60 + "\n")

# Проверить ожидаемый результат
with open('tests/expected_output/example_one_daily_summary.txt', 'r') as f:
    expected = f.read()

print("Ожидаемый результат:")
print(expected)

print("\n" + "="*60 + "\n")

# Сравнить
if result == expected:
    print("✅ РЕЗУЛЬТАТ СОВПАДАЕТ!")
else:
    print("❌ РЕЗУЛЬТАТ НЕ СОВПАДАЕТ!")
    print("\nРазница:")
    print(f"Получено ({len(result)} символов):\n{repr(result)}")
    print(f"\nОжидается ({len(expected)} символов):\n{repr(expected)}")
