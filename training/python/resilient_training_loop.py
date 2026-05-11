import csv

dataset = []
skipped_rows = 0

with open("../../data/customers.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            features = [
                float(row["age"]),
                float(row["monthly_income"]),
                float(row["years_experience"]),
            ]

            label = int(row["purchased"])

            dataset.append((features, label))

        except ValueError as error:
            skipped_rows += 1
            print(f"Skipped row {row['id']} during loading -> {error}")

for epoch in range(1, 4):
    print(f"\nEpoch {epoch}")

    for index, (features, label) in enumerate(dataset, start=1):
        try:
            prediction = sum(features) / len(features)
            loss = abs(prediction - label)

            print(f"Batch {index}: loss={loss:.2f}")

        except Exception as error:
            print(f"Failed batch {index} -> {error}")

        finally:
            pass

print("\nTraining Summary")
print(f"Valid samples used: {len(dataset)}")
print(f"Skipped rows: {skipped_rows}")
