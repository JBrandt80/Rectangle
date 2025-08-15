# Jeffrey Brandt
# CIS261
# Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def calculate_area(self):
        return self.height * self.width

    def print_rectangle(self):
        print("\nRectangle:")
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("* " * self.width)
            else:
                print("* " + "  " * (self.width - 2) + "*")

def main():
    print("Welcome to the Rectangle Calculator!")
    print()
    try:
        height = int(input("Enter the height of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        
        rect = Rectangle(height, width)

        print(f"\nPerimeter: {rect.calculate_perimeter()}")
        print(f"Area: {rect.calculate_area()}")
        rect.print_rectangle()

    except ValueError:
        print("Please enter valid integer values for height and width>")

if __name__ == "__main__":
    main()
