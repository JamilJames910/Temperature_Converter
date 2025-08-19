# Temperature Converter 🌡️
A Python script to convert temperatures between Celsius and Fahrenheit. Perfect for quick conversions, learning Python, or practicing CLI programs.

## Features ✨
✅ Convert Celsius to Fahrenheit.  
✅ Convert Fahrenheit to Celsius.  
✅ Interactive command-line interface.  
✅ Option to quit at any time.  
✅ Handles invalid input gracefully.  

## Table of Contents
Installation  
Usage  
Key Functions  
Example  
Project Structure  
Contributing  
Contact  

## Installation 🛠️
Clone this repository:

```bash
git clone https://github.com/JamilJames910/Temperature_Converter.git
cd Temperature_Converter
````

Make sure you have Python 3.x installed.

No additional dependencies are required—Python's built-in functions handle everything.

## Usage 💻

Run the script:

```bash
python Temperature_Converter.py
```

You can also use the functions in your own scripts:

```python
from Temperature_Converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print(celsius_to_fahrenheit(25))  # 25°C → 77°F
print(fahrenheit_to_celsius(77))  # 77°F → 25°C
```

## Key Functions

`celsius_to_fahrenheit(celsius)`: Convert Celsius to Fahrenheit.

`fahrenheit_to_celsius(fahrenheit)`: Convert Fahrenheit to Celsius.

## Example

Interactive usage:

```
Welcome to the Temperature Converter!
Type 'quit' at any time to exit.

Convert from (C)elsius or (F)ahrenheit? C
Enter temperature in Celsius: 100
100°C is equal to 212.0°F

Convert from (C)elsius or (F)ahrenheit? F
Enter temperature in Fahrenheit: 32
32°F is equal to 0.0°C

Convert from (C)elsius or (F)ahrenheit? quit
Goodbye!
```

## Project Structure 🗂️

```
Temperature_Converter
├── Temperature_Converter.py   # Main script
├── README.md                  # Project documentation
└── .gitignore                 # Git ignore file
```

## Contributing 🤝

Contributions, suggestions, and improvements are welcome!

Fork the repository.
Create a feature branch: `git checkout -b feature-name`.
Commit your changes: `git commit -m "Add feature"`.
Push to the branch: `git push origin feature-name`.
Open a Pull Request.

## Contact ✉️

Created with ❤️ by Jamil James

GitHub: [JamilJames910](https://github.com/JamilJames910)
Email: [Jamil.i.James1@gmail.com](mailto:Jamil.i.James1@gmail.com)

