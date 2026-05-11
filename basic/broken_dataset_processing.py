import csv

with open("../../data/customers.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        age = int(row["age"])
        income = float(row["monthly_income"])

        score = age * income

        print(f"Processed customer {row['id']} -> score={score}")
