# C# Error Handling — Beyond try/catch

Most developers use `try/catch`.
Very few design error handling as a system. This repository demonstrates how to move from basic exception handling to structured, production-ready error design to help determine the error roots faster, using C# as a reference implementation.

---

## Overview

This project focuses on designing how errors are handled across an application, not just catching exceptions.

It covers:

* Meaningful exception design
* Adding context to errors
* Centralized error handling
* Logging strategies
* Avoiding common anti-patterns
* Using result patterns where appropriate

The goal is to make failures understandable, traceable, and recoverable.

---

## Problem

Many codebases:

* Catch `Exception` without context
* Lose stack trace information
* Mix user-facing and system-level messages
* Lack consistent logging
* Use exceptions for normal control flow

This leads to systems that are difficult to debug and maintain.

---

## Approach

Error handling is treated as a system with clear responsibilities:

* Domain layer: defines meaningful exceptions
* Application layer: adds context and coordinates logic
* Infrastructure layer: handles logging and persistence
* Presentation layer: displays safe user messages

---

## Project Structure

```bash
src/
 ├── Domain/
 │    └── Exceptions/
 │
 ├── Application/
 │    ├── Services/
 │    └── Results/
 │
 ├── Infrastructure/
 │    ├── Logging/
 │    └── ErrorHandling/
 │
 └── Presentation/
```


## Contributing

Contributions are welcome. Suggestions for improvements or additional patterns are encouraged.

---

