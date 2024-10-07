# Exercise 1: Student Grades Analysis
print("-----Exercise 1-----")

students = {
    "Alice": [85, 78, 92],
    "Bob": [79, 74, 81],
    "Charlie": [91, 82, 85],
    "David": [76, 85, 83],
    "Eve": [88, 79, 92]
}

# Task 1: Calculate and print the average score for each student.
for student, scores in students.items():
    total_score = sum(scores)
    average = total_score / len(scores)
    print(f"* {student}'s average score is {average}")

# Task 2: Find and print the name of the student with the highest average score.
highest_avg_student = ""
highest_avg_score = 0
for student, scores in students.items():
    average_score = sum(scores) / len(scores)
    if average_score > highest_avg_score:
        highest_avg_score = average_score
        highest_avg_student = student

print(f"* The student with the highest average score is {highest_avg_student} with an average score of {highest_avg_score}")

# Task 3: Find and print the name of the student with the lowest average score.
lowest_avg_student =  ""
lowest_avg_score = float('inf')
for student, scores in students.items():
    average_score = sum(scores) / len(scores)
    if average_score < lowest_avg_score:
        lowest_avg_score = average_score
        lowest_avg_student = student

print(f"* The student with the lowest average score is {lowest_avg_student} with an average score of {lowest_avg_score}")

# Task 4: Add a new student "Frank" with scores [80, 90, 85] to the dictionary and print the updated dictionary.
students["Frank"] = [80, 90, 85]
print("* Updated students dictionary:", students)

# Exercise 2: Product Inventory Management
print("-----Exercise 2-----")
inventory = {
    "apple": (50, 0.5),
    "banana": (100, 0.2),
    "orange": (75, 0.3),
    "pear": (20, 0.4)
}

# Task 1: Print the current inventory in a user-friendly format.
for product, details in inventory.items():
    print(f"* {product.capitalize()}: Quantity = {details[0]}, Price per unit = ${details[1]}")

# Task 2: Calculate and print the total value of the inventory.
total_value = 0
for item, (quantity, price) in inventory.items():
    total_value += quantity * price

print(f"* Total value of the inventory is: ${total_value}")

# Task 3: Add a new product "mango" with 30 items priced at $0.6 each to the inventory.
inventory["mango"] = (30, 0.6)
print("* Inventory after adding mango:", inventory)

# Task 4: Update the quantity of "banana" to 120 and print the updated inventory.
inventory["banana"] = (120, inventory["banana"][1])
print("* Inventory after updating banana quantity:", inventory)

# Task 5: Remove "pear" from the inventory and print the updated inventory.
inventory.pop("pear")
print("* Inventory after removing pear:", inventory)

# Exercise 3: Employee Records
print("-----Exercise 3-----")

employees = [
    ("John Doe", "Accounting", "john.doe@example.com"),
    ("Jane Smith", "Marketing", "jane.smith@example.com"),
    ("Emily Davis", "HR", "emily.davis@example.com"),
    ("Michael Brown", "IT", "michael.brown@example.com")
]

# Task 1: Print the names and departments of all employees.
for name, department, _ in employees:
    print(f"* {name} works in {department}")

# Task 2: Print the email addresses of all employees in alphabetical order by their last names.
def get_last_name(employee):
    full_name = employee[0]
    last_name = full_name.split()[-1]
    return last_name

employees.sort(key=get_last_name)
emails = [employee[2] for employee in employees]
print("* Emails in alphabetical order by last name:", emails)

# Task 3: Add a new employee ("David Wilson", "Sales", "david.wilson@example.com") and print the updated list.
employees.append(("David Wilson", "Sales", "david.wilson@example.com"))
print("* Updated employee list:", employees)

# Task 4: Find and print the department of "Jane Smith".
jane_department = ""
for employee in employees:
    name, department, _ = employee
    if name == "Jane Smith":
        jane_department = department
        break

print(f"* Jane Smith works in {jane_department}")

# Exercise 4: Book Library System
print("-----Exercise 4-----")

library = {
    "978-3-16-148410-0": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951},
    "978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
    "978-0-7432-7356-5": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    "978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}
}

# Task 1: Print the details of all books in a user-friendly format.
for isbn, details in library.items():
    print(f"* ISBN: {isbn} - Title: {details['title']}, Author: {details['author']}, Year: {details['year']}")

# Task 2: Find and print the details of the book with the ISBN "978-0-14-028329-7".
book_1984 = library.get("978-0-14-028329-7")
print("* Details of the book with ISBN 978-0-14-028329-7:", book_1984)

# Task 3: Add a new book with ISBN "978-1-4028-9462-6", title "The Great Gatsby", author "F. Scott Fitzgerald", and year 1925.
library["978-1-4028-9462-6"] = {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
print("* Library after adding The Great Gatsby:", library)

# Task 4: Update the year of "To Kill a Mockingbird" to 1961 and print the updated details.
library["978-0-7432-7356-5"]["year"] = 1961
print("* Updated details of 'To Kill a Mockingbird':", library["978-0-7432-7356-5"])

# Task 5: Remove the book with ISBN "978-0-452-28423-4" and print the updated library.
library.pop("978-0-452-28423-4")
print("* Library after removing Brave New World:", library)

# Exercise 5: City Population Data
print("-----Exercise 5-----")

cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}

# Task 1: Print the population of each city in a user-friendly format.
for city, population in cities.items():
    print(f"* The population of {city} is {population:,}")

# Task 2: Find and print the city with the highest population.
highest_population_city = max(cities, key=cities.get)
print(f"* The city with the highest population is {highest_population_city}")

# Task 3: Find and print the city with the lowest population.
lowest_population_city = min(cities, key=cities.get)
print(f"* The city with the lowest population is {lowest_population_city}")

# Task 4: Update the population of "Phoenix" to 1,700,000 and print the updated data.
cities["Phoenix"] = 1700000
print("* Updated city data after changing Phoenix population:", cities)

# Task 5: Add a new city "San Francisco" with a population of 884,000 and print the updated data.
cities["San Francisco"] = 884000
print("* Updated city data after adding San Francisco:", cities)

# Exercise 6: Movie Database
print("-----Exercise 6-----")

movies = {
    "Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
    "The Godfather": {"year": 1972, "rating": 9.2, "genre": "Crime"},
    "The Dark Knight": {"year": 2008, "rating": 9.0, "genre": "Action"},
    "Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
    "Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}

# Task 1: Print the details of all movies in a user-friendly format.
for movie, details in movies.items():
    print(f"* Title: {movie}, Year: {details['year']}, Rating: {details['rating']}, Genre: {details['genre']}")

# Task 2: Find and print the highest-rated movie.
def get_movie_rating(movie_name):
    return movies[movie_name]["rating"]

highest_rated_movie = max(movies, key=get_movie_rating)
print(f"* The highest-rated movie is {highest_rated_movie}")

# Task 3: Add a new movie "The Matrix" with year 1999, rating 8.7, and genre "Sci-Fi" to the database.
movies["The Matrix"] = {"year": 1999, "rating": 8.7, "genre": "Sci-Fi"}
print("* Movie database after adding The Matrix:", movies)

# Task 4: Update the rating of "Inception" to 9.0 and print the updated details.
movies["Inception"]["rating"] = 9.0
print("* Updated details of 'Inception':", movies["Inception"])

# Task 5: Remove "Pulp Fiction" from the database and print the updated list.
movies.pop("Pulp Fiction")
print("* Movie database after removing Pulp Fiction:", movies)

# Exercise 7: Country Capitals
print("-----Exercise 7-----")

countries = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo"
}

# Task 1: Print the names of all countries and their capitals.
for country, capital in countries.items():
    print(f"* The capital of {country} is {capital}")

# Task 2: Find and print the capital of Germany.
germany_capital = countries.get("Germany")
print(f"* The capital of Germany is {germany_capital}")

# Task 3: Add a new country "Australia" with capital "Canberra" to the dictionary and print the updated dictionary.
countries["Australia"] = "Canberra"
print("* Updated countries dictionary:", countries)

# Task 4: Update the capital of "USA" to "New Washington" and print the updated dictionary.
countries["USA"] = "New Washington"
print("* Updated countries dictionary after changing USA capital:", countries)

# Task 5: Remove "France" from the dictionary and print the updated dictionary.
countries.pop("France")
print("* Countries dictionary after removing France:", countries)

# Exercise 8: Shopping Cart
print("-----Exercise 8-----")

cart = [
    {"item": "apple", "quantity": 3, "price_per_unit": 0.5},
    {"item": "banana", "quantity": 6, "price_per_unit": 0.2},
    {"item": "orange", "quantity": 4, "price_per_unit": 0.3},
    {"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]

# Task 1: Print the details of all items in the cart.
for product in cart:
    print(f"* Item: {product['item']}, Quantity: {product['quantity']}, Price per unit: ${product['price_per_unit']}")

# Task 2: Calculate and print the total cost of the cart.
total_cost = sum(item['quantity'] * item['price_per_unit'] for item in cart)
print(f"* Total cost of the cart is: ${total_cost:.2f}")

# Task 3: Add a new item "grape" with quantity 5 and price per unit 0.6 to the cart.
cart.append({"item": "grape", "quantity": 5, "price_per_unit": 0.6})
print("* Cart after adding grape:", cart)

# Task 4: Update the quantity of "banana" to 10 and print the updated cart.
for product in cart:
    if product["item"] == "banana":
        product["quantity"] = 10
print("* Cart after updating banana quantity:", cart)

# Task 5: Remove "pear" from the cart and print the updated cart.
updated_cart = []
for product in cart:
    if product["item"] != "pear":
        updated_cart.append(product)

print("* Cart after removing pear:", updated_cart)

# Exercise 9: Weather Data
print("-----Exercise 9-----")

weather = {
    "Monday": {"temperature": 20, "humidity": 60},
    "Tuesday": {"temperature": 22, "humidity": 55},
    "Wednesday": {"temperature": 19, "humidity": 65},
    "Thursday": {"temperature": 23, "humidity": 50},
    "Friday": {"temperature": 21, "humidity": 70}
}

# Task 1: Print the weather details for each day.
for day, details in weather.items():
    print(f"* {day}: Temperature = {details['temperature']}°C, Humidity = {details['humidity']}%")

# Task 2: Find and print the day with the highest temperature using a custom function
def get_temperature(day_name):
    return weather[day_name]["temperature"]

highest_temp_day = max(weather, key=get_temperature)
print(f"* The day with the highest temperature is {highest_temp_day}")

# Task 3: Find and print the day with the lowest humidity using a custom function
def get_humidity(day_name):
    return weather[day_name]["humidity"]

lowest_humidity_day = min(weather, key=get_humidity)
print(f"* The day with the lowest humidity is {lowest_humidity_day}")

# Task 4: Update the temperature of "Wednesday" to 25 and print the updated weather data.
weather["Wednesday"]["temperature"] = 25
print("* Updated weather data after changing Wednesday's temperature:", weather)

# Task 5: Add weather data for "Saturday" with temperature 24 and humidity 60 to the dictionary and print the updated weather data.
weather["Saturday"] = {"temperature": 24, "humidity": 60}
print("* Updated weather data after adding Saturday:", weather)

# Task 10: Library Members
print("-----Task 10-----")

members = [
    {"name": "Alice", "age": 25, "books_borrowed": ["1984", "To Kill a Mockingbird"]},
    {"name": "Bob", "age": 30, "books_borrowed": ["The Catcher in the Rye"]},
    {"name": "Charlie", "age": 22, "books_borrowed": ["Brave New World", "1984"]},
    {"name": "David", "age": 35, "books_borrowed": ["The Great Gatsby"]}
]

# Task 1: Print the names and ages of all members.
for member in members:
    print(f"* Name: {member['name']}, Age: {member['age']}")

# Task 2: Find and print the books borrowed by "Charlie".
charlie_books = ""
for member in members:
    if member['name'] == "Charlie":
        charlie_books = member['books_borrowed']
        break

print(f"* Books borrowed by Charlie: {charlie_books}")

# Task 3: Add a new member "Eve" with age 28 and books borrowed ["Pride and Prejudice"] to the list.
members.append({"name": "Eve", "age": 28, "books_borrowed": ["Pride and Prejudice"]})
print("* Updated members list after adding Eve:", members)

# Task 4: Update the age of "Bob" to 31 and print the updated list.
for member in members:
    if member['name'] == "Bob":
        member['age'] = 31
print("* Updated members list after changing Bob's age:", members)

# Task 5: Remove "David" from the members list and print the updated list.
updated_members = []
for member in members:
    if member['name'] != "David":
        updated_members.append(member)

print("* Updated members list after removing David:", updated_members)