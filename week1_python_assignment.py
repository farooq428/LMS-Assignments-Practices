# PROGRAM 01 | Cinema Ticket Calculator

age = int(input("Enter Your Age: "))
tickets = int(input("Enter Number of tickets: "))

charges = 0
if age >= 12:
    price = tickets * 300;
    print("Your Total cost is: " , price)
else:
    price = tickets * 180;
    print("Your total cost is: " , price)




# PROGRAM 02 | Name Tag Generator

first_name = str(input("Enter Your First Name: ")).strip()
last_name = str(input("Enter Your Last Name: ")).strip()


full_name = first_name.title() + " "  + last_name.title()




print("Your Name is:" , full_name)     

initials = first_name[0].upper() + "." + last_name[0].upper() + "."

print(f"initials: {initials}")

total_letters = len(first_name) + len(last_name)

print(f"Total letters excluding space: {total_letters}")




# Program 3

steps = []

for day in range(1 , 6):
    daily_steps = int(input(f"Enter steps of day {day} :"))
    steps.append(daily_steps)

total_steps = sum(steps)   

print(total_steps);

max_steps = max(steps)

print(max_steps)

avg_steps = total_steps / len(steps)

print(f"Average steps: {avg_steps}")

qualifying_steps = 0

for daily_steps in steps:
    if(daily_steps >= 6000):
        qualifying_steps += 1
print(f"{qualifying_steps} days have 6000 or more then 6000 steps")       



# program 4

prices = {
    "pen": 50,
    "notebook": 200,
    "eraser": 30,
}

item = input("Enter item name that you want to update: ").strip().lower()

if item in prices:
    new_price = float(input("Enter the new price: "))

    # Step 3: Update the item's price
    prices.update({item: new_price})
else:
    print("Item not found!")


print("\n--- Updated Stationery Prices ---")

for item, price in prices.items():
    print(f"{item.title()}: Rs. {price:g}")

total_price = sum(prices.values())

print(f"Total price: Rs. {total_price:g}")




#  PROGRAM 05 | Three-Subject Result Checker

def average_marks(a: int, b: int, c: int) -> float:
    """Calculate the average of three subject marks."""
    return (a + b + c) / 3


# Take marks from the user
mark1 = int(input("Enter marks for subject 1: "))
mark2 = int(input("Enter marks for subject 2: "))
mark3 = int(input("Enter marks for subject 3: "))

# Calculate average
average = average_marks(mark1, mark2, mark3)

print("Average marks:", average)

# Check result
if average >= 50:
    print("Pass")
else:
    print("Needs improvement")

# Test the function
assert average_marks(60, 70, 80) == 70.0
print("Function test passed!")



# Program 06: Visitor Register

# Ask for two visitors' names
visitor1 = input("Enter the first visitor's name: ")
visitor2 = input("Enter the second visitor's name: ")

# Write the first visitor's name
with open("visitors.txt", "w") as file:
    file.write(visitor1.strip() + "\n")

# Append the second visitor's name
with open("visitors.txt", "a") as file:
    file.write(visitor2.strip() + "\n")

# Read and display both names
with open("visitors.txt", "r") as file:
    visitors = file.read()

print("\nVisitor Register:")
print(visitors)



# Program 07: Movie Watchlist with JSON

import json

# Create a list of three movies
movies = [
    {"title": "Avengers", "watched": True},
    {"title": "Interstellar", "watched": False},
    {"title": "Inception", "watched": False}
]

# Save movies to a JSON file
with open("watchlist.json", "w") as file:
    json.dump(movies, file, indent=4)

print("Watchlist saved successfully!")

# Load movies from the JSON file
with open("watchlist.json", "r") as file:
    loaded_movies = json.load(file)

# Print the second movie's title
print("\nSecond movie:", loaded_movies[1]["title"])

# Print movies that have not been watched
print("\nMovies not yet watched:")

for movie in loaded_movies:
    if movie["watched"] == False:
        print(movie["title"])




# Program 08: Shared-Bill Calculator

try:
    # Take input from the user
    bill = float(input("Enter the total restaurant bill: "))
    friends = int(input("Enter the number of friends sharing the bill: "))

    # Validate the number of friends
    if friends <= 0:
        print("Error: The number of friends must be greater than zero.")

    elif bill < 0:
        print("Error: The bill cannot be negative.")

    else:
        # Calculate each person's share
        share = bill / friends

        print(f"Each person should pay: Rs. {share:.2f}")

except ValueError:
    print("Invalid input! Please enter numbers only.")



# Program 09: Parcel Delivery Classes

# Create the parent class
class Parcel:
    def __init__(self, item_name: str, weight: float):
        self.item_name = item_name
        self.weight = weight

    def delivery_fee(self) -> float:
        return self.weight * 50


# Create the child class
class ExpressParcel(Parcel):
    def delivery_fee(self) -> float:
        return self.weight * 80


# Create objects
normal_parcel = Parcel("Books", 2)
express_parcel = ExpressParcel("Laptop", 2)

# Display delivery fees
print("Normal parcel fee:", normal_parcel.delivery_fee())
print("Express parcel fee:", express_parcel.delivery_fee())



# Program 10: Book Club Database

import sqlite3

# Create or open the database
db = sqlite3.connect("book_club.db")

# Create the members table if it does not exist
db.execute("""
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
""")

# Insert two members using parameterized queries
db.execute(
    "INSERT INTO members (name) VALUES (?)",
    ("Ali",)
)

db.execute(
    "INSERT INTO members (name) VALUES (?)",
    ("Ahmed",)
)

# Save changes
db.commit()

# Read all member names
cursor = db.execute("SELECT name FROM members")
members = cursor.fetchall()

# Check that at least two members exist
assert len(members) >= 2, "At least two members are required!"

# Display member names
print("Book Club Members:")

for member in members:
    print(member[0])

# Close the database connection
db.close()



