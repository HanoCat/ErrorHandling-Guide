using System;
using System.IO;
using System.Collections.Generic;

var dataset = new List<(double[] Features, int Label)>();

var lines = File.ReadAllLines("../../data/customers.csv");

foreach (var line in lines[1..])
{
    var columns = line.Split(',');

    var features = new double[]
    {
        double.Parse(columns[1]),
        double.Parse(columns[2]),
        double.Parse(columns[3])
    };

    var label = int.Parse(columns[4]);

    dataset.Add((features, label));
}

for (int epoch = 1; epoch <= 3; epoch++)
{
    Console.WriteLine($"\nEpoch {epoch}");

    int batch = 1;

    foreach (var sample in dataset)
    {
        var prediction =
            (sample.Features[0] +
             sample.Features[1] +
             sample.Features[2]) / 3;

        var loss = Math.Abs(prediction - sample.Label);

        Console.WriteLine($"Batch {batch}: loss={loss:F2}");

        batch++;
    }
}
