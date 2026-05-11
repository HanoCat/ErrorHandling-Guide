using System;
using System.IO;

var lines = File.ReadAllLines("../../data/customers.csv");

int processedRows = 0;
int failedRows = 0;

foreach (var line in lines[1..])
{
    try
    {
        var columns = line.Split(',');

        var id = columns[0];
        var age = int.Parse(columns[1]);
        var income = double.Parse(columns[2]);

        var score = age * income;

        Console.WriteLine($"Processed customer {id} -> score={score}");
    }
    catch (Exception error)
    {
        failedRows++;

        Console.WriteLine($"Failed row -> {error.Message}");
    }
    finally
    {
        processedRows++;
    }
}

Console.WriteLine("\nSummary");
Console.WriteLine($"Processed rows: {processedRows}");
Console.WriteLine($"Failed rows: {failedRows}");
