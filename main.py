# 1. List of users only from Poland
users = [
    {"name": "Kamil", "country": "Poland"},
    {"name": "John", "country": "USA"},
    {"name": "Yeti"}
]
polish_users = [user for user in users if user.get('country') == "Poland"]
print("Polish users:", polish_users)

# 2. Sum of 10 elements, starting with element 5
numbers = [1, 5, 2, 3, 1, 4, 1, 23, 12, 2, 3, 1, 2, 31, 23, 1, 2, 3, 1, 23, 1, 2, 3, 123]
sum_of_elements = sum(numbers[5:15])
print("Sum of elements:", sum_of_elements)

# 3. List of powers of 2 for n from 1 to 20
powers_of_two = [2 ** n for n in range(1, 21)]
print("Powers of 2:", powers_of_two)
