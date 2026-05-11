import csv

dataset = []

with open("../../data/customers.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        features = [
            float(row["age"]),
            float(row["monthly_income"]),
            float(row["years_experience"]),
        ]

        label = int(row["purchased"])

        dataset.append((features, label))


for epoch in range(1, 4):
    print(f"\nEpoch {epoch}")

    for index, (features, label) in enumerate(dataset, start=1):
        prediction = sum(features) / len(features)
        loss = abs(prediction - label)

        print(f"Batch {index}: loss={loss:.2f}")
