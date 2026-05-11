# The Bug Was Cheap. The Debugging Was Expensive.

This repository accompanies the Medium article discussing why failure handling matters more than most developers think. The examples here focus on practical scenarios where failures become expensive because they are invisible, difficult to trace, or handled too late. Instead of treating exceptions as a language feature, the goal is to demonstrate how proper error handling improves observability, recovery, debugging, and trust.

The repository includes examples in both Python and C#.
## Current Examples

### Broken Dataset Processing

A minimal example showing how a single malformed value can terminate an entire processing pipeline.

```bash
python python/basic/broken_dataset_processing.py
```

### Resilient Dataset Processing

A safer version that isolates failures, continues processing valid rows, and preserves visibility into corrupted data.

```bash
python python/basic/resilient_dataset_processing.py
```


## Clone the Repository

```bash
git clone https://github.com/HanoCat/ErrorHandling-Guide.git

cd ErrorHandling-Guide
```
