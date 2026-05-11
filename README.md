# The Bug Was Cheap. The Debugging Was Expensive.

This repository accompanies the Medium article discussing why failure handling matters more than most developers think. The examples here focus on practical scenarios where failures become expensive because they are invisible, difficult to trace, or handled too late. Instead of treating exceptions as a language feature, the goal is to demonstrate how proper error handling improves observability, recovery, debugging, and trust.

The repository includes examples in both Python and C#. The `basic` section contains simple examples demonstrating how fragile processing pipelines fail compared to resilient implementations that isolate and recover from corrupted input. The `training` section simulates long-running training loops where invalid data, missing values, or unexpected failures can interrupt computation and waste significant execution time if errors are not handled intentionally.

## Repository Structure

```text
ErrorHandling-Guide/
│
├── data/
│   └── customers.csv
│
├── basic/
│   ├── python/
│   │   ├── broken_dataset_processing.py
│   │   └── resilient_dataset_processing.py
│   │
│   └── csharp/
│       ├── BrokenDatasetProcessing.cs
│       └── ResilientDatasetProcessing.cs
│
├── training/
│   ├── python/
│   │   ├── broken_training_loop.py
│   │   └── resilient_training_loop.py
│   │
│   └── csharp/
│       ├── BrokenTrainingLoop.cs
│       └── ResilientTrainingLoop.cs
│
└── README.md
```



## Clone the Repository

```bash
git clone https://github.com/HanoCat/ErrorHandling-Guide.git

cd ErrorHandling-Guide
```
