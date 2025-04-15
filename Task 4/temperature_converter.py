def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9


def main():
    """Main function to run the temperature converter."""
    print("🌡️ Temperature Converter")

    while True:
        print("\nChoose conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "2":
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")
            except ValueError:
                print("❌ Please enter a valid number.")

        elif choice == "3":
            print("👋 Exiting Temperature Converter. Goodbye!")
            break

        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
