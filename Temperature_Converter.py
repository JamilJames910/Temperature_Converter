def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 

# Main program
def main(): 
    print("Welcome to the Temperature Converter!")
    print("Type 'quit' at any time to exit. \n")

    while True: 
        choice = input("Convert from (C)elsius or (F)ahrenheit?").lower()
        
        if choice == 'quit':
            print("Goodbye!")
            break

        if choice == 'c':
            temp = input("Enter temperature in Celsius:")
            if temp.lower() == 'quit':
                print("Goodbye!")
                break
            c = float(temp)
            f = celsius_to_fahrenheit(c)
            print(f"{c}°C is equal to {round(f, 2)}°F")
        
        elif choice == 'f':
            temp = input("Enter temperature in Fahrenheit: ")
            if temp.lower() == 'quit': 
                print("Goodbye!")
                break
            f = float(temp)
            c = fahrenheit_to_celsius(f)
            print(f"{f}°F is equal to {round(c,2)}°C\n")
        else: 
            print("Invalid choice. Please enter 'C','F', or 'quit' .\n")

# Run the program
main()