# Temperature Converter

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)  

A simple, interactive command-line **Temperature Converter** built in Python that allows users to convert temperatures between Celsius and Fahrenheit. This project is designed to be user-friendly, robust, and easily extendable for future enhancements.

---

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Project Overview

Temperature conversion is a common task in scientific, engineering, and everyday contexts. This project provides an easy-to-use command-line interface that allows users to quickly convert between Celsius and Fahrenheit.  

It demonstrates:
- Clean and readable Python code
- Interactive command-line experience
- Proper input handling with graceful exits

---

## Features

- Convert temperatures from **Celsius to Fahrenheit**
- Convert temperatures from **Fahrenheit to Celsius**
- Continuous interaction until the user decides to quit
- Handles invalid input gracefully
- Simple, human-readable output for clarity

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/JamilJames910/Temperature_Converter.git
````

2. **Navigate to the project folder:**

```bash
cd temperature-converter
```

3. **Ensure Python is installed** (Python 3.7+ recommended):

```bash
python --version
```

---

## Usage

Run the program in the terminal:

```bash
python temperature_converter.py
```

**Example Interaction:**

```
Welcome to the Temperature Converter!
Type 'quit' at any time to exit.

Convert from (C)elsius or (F)ahrenheit? c
Enter temperature in Celsius: 100
100.0°C is equal to 212.0°F

Convert from (C)elsius or (F)ahrenheit? f
Enter temperature in Fahrenheit: 32
32.0°F is equal to 0.0°C
```

Type `'quit'` at any prompt to exit the program.

---

## Code Structure

```
temperature_converter.py
│
├─ celsius_to_fahrenheit(celsius)    # Converts Celsius to Fahrenheit
├─ fahrenheit_to_celsius(fahrenheit) # Converts Fahrenheit to Celsius
└─ main()                            # Main interactive program loop
```

* **Functions** are modular, enabling easy reuse and testing.
* Input validation ensures smooth user experience.

---

## Contributing

Contributions are welcome! Here’s how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Make your changes
4. Commit your work (`git commit -m "Add feature"`)
5. Push to the branch (`git push origin feature-name`)
6. Open a Pull Request
