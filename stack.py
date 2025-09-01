class Stack:
    def __init__(self):
        self.s = []

    # Method to push item onto the stack
    def push(self, item):
        self.s.append(item)
        print(f'"{item}" pushed onto the stack.')

    # Method to check if the stack is empty
    def is_empty(self):
        return len(self.s) == 0

    # Method to pop an item from the stack
    def pop(self):
        if self.is_empty():
            print("Underflow! Stack is empty.")
        else:
            val = self.s.pop()
            print(f'"{val}" popped from the stack.')
            return val

    # Method to peek at the top item of the stack
    def peek(self):
        if self.is_empty():
            print("Underflow! Stack is empty.")
        else:
            print(f'Top item is: "{self.s[-1]}"')
            return self.s[-1]

    # Method to show all items in the stack
    def show(self):
        if self.is_empty():
            print("Sorry, no items in the stack.")
        else:
            print("(Top) ", end='')
            for item in reversed(self.s):
                print(f"{item} <== ", end='')
            print()

    # Method to display menu and handle user choices
    def choice(self):
        while True:
            print("\nStack Operations Menu:")
            print("1. Push an item")
            print("2. Pop the item")
            print("3. Peek the stack")
            print("4. Show the stack")
            print("5. Exit ")
            try:
                opt = int(input("Enter your choice: "))
                if opt == 1:
                    item = input("Enter the item you want to push: ")
                    self.push(item)
                elif opt == 2:
                    self.pop()
                elif opt == 3:
                    self.peek()
                elif opt == 4:
                    self.show()
                elif opt == 5:
                    print("**** PROGRAM ENDS HERE ****")
                    break
                else:
                    print("Invalid choice. Please select 1–5.")
            except ValueError:
                print("Please enter a valid number.")

# Create an object of Stack
stack_obj = Stack()
# Call the menu method
stack_obj.choice()

