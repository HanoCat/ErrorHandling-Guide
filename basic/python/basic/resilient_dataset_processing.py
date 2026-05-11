import csv

processed_rows = 0
failed_rows = 0

with open("../../data/customers.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            age = int(row["age"])
            income = float(row["monthly_income"])

            score = age * income

            print(f"Processed customer {row['id']} -> score={score}")

        except ValueError as error:
            failed_rows += 1
            print(f"Failed customer {row['id']} -> {error}")

        finally:
            processed_rows += 1

print("\nSummary")
print(f"Processed rows: {processed_rows}")
print(f"Failed rows: {failed_rows}")
