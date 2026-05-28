from weather import generate_daily_summary, load_data_from_csv

# Load data from CSV
data = load_data_from_csv('tests/data/example_one.csv')

print("Loaded data:")
print(data)
print("\n" + "="*60 + "\n")

# Call the function
result = generate_daily_summary(data)

print("Result of generate_daily_summary():")
print(result)

print("\n" + "="*60 + "\n")

# Check expected output
with open('tests/expected_output/example_one_daily_summary.txt', 'r') as f:
    expected = f.read()

print("Expected output:")
print(expected)

print("\n" + "="*60 + "\n")

# Compare
if result == expected:
    print("✅ RESULT MATCHES!")
else:
    print("❌ RESULT DOES NOT MATCH!")
    print("\nDifference:")
    print(f"Received ({len(result)} characters):\n{repr(result)}")
    print(f"\nExpected ({len(expected)} characters):\n{repr(expected)}")
