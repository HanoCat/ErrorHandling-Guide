using System;
using System.IO;

var lines = File.ReadAllLines("../../data/customers.csv");

foreach (var line in lines[1..])
{
    var columns = line.Split(',');

    var id = columns[0];
    var age = int.Parse(columns[1]);
    var income = double.Parse(columns[2]);

    var score = age * income;

    Console.WriteLine($"Processed customer {id} -> score={score}");
}
