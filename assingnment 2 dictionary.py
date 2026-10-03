# 1. List Creation
age_list = [24, 25, 26, 27, 28]
name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 2. List Operations / Modifications

# a. Append the string "Yazhini" to name_list.
name_list.append("Yazhini")

# b. Insert the element 30 at index 2 in age_list.
age_list.insert(2, 30)

# c. Remove the string "Yazhini" from name_list.
name_list.remove("Yazhini")

# d. Pop the last element from age_list.
age_list.pop()

# e. Extend the age_list with additional ages [29, 30, 26].
age_list.extend([29, 30, 26])

# f. Sort age_list in descending order.
age_list.sort(reverse=True)

# g. Find Max age, Min age and sum of all ages from age_list.
max_age = max(age_list)
min_age = min(age_list)
sum_ages = sum(age_list)

print(f"Max age: {max_age}")
print(f"Min age: {min_age}")
print(f"Sum of all ages: {sum_ages}")
# Assuming name_list from the previous section
name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# 3. Accessing List Elements

# a. Print the first element of name_list.
print(name_list[0])

# b. Print the last element of name_list.
print(name_list[-1])

# c. Print the elements from index 2 to index 4 in name_list.
# (Slicing [2:5] includes indices 2, 3, and 4)
print(name_list[2:5])

# d. Print the elements of name_list in reverse order.
print(name_list[::-1])


# Dictionary (Creation, Modification and Access)

# a. Create a dictionary named student_marks that maps the names of five students to their marks.
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}

# b. Access and print the mark of a specific student, of your choice.
print(f"Charlie's mark is: {student_marks['Charlie']}")

# c. Add a new student "Janani" with a mark of 80 to the student_marks dictionary.
student_marks["Janani"] = 80

# d. Update the mark of any one older student to 82.
student_marks["Bob"] = 82
# Assuming student_marks from the previous section
student_marks = {"Alice": 85, "Bob": 82, "Charlie": 78, "David": 95, "Eve": 88, "Janani": 80}

# e. Use keys(), values(), and items() methods
print("Keys:", student_marks.keys())
print("Values:", student_marks.values())
print("Key-Value Pairs (Items):", student_marks.items())


# Sets (Operations)

# a. Create a set called my_set and analyze the output
my_set = set(['a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'])
print(f"\nmy_set output: {my_set}")
# Explanation: The output only shows unique elements ({'o', 'e', 'a', 'u', 'i'} - order may vary). 
# This is because sets in Python are unordered collections of unique elements and automatically remove duplicates.

# b. Attempt to change the value of my_set[4] = 's'
try:
    my_set[4] = 's'
except TypeError as e:
    print(f"\nError encountered: {e}")
    # Explanation: The code throws a TypeError ("'set' object does not support item assignment").
    # Sets are unordered, meaning elements do not have a specific index (like lists or tuples do). 
    # Therefore, you cannot access or modify set elements using an index.

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Compute and print the union and intersection of set1 and set2
union_set = set1.union(set2)
# Alternatively: union_set = set1 | set2

intersection_set = set1.intersection(set2)
# Alternatively: intersection_set = set1 & set2

print(f"\nUnion of set1 and set2: {union_set}")
print(f"Intersection of set1 and set2: {intersection_set}")
# Operators & Conditional Statements (IF, ELIF, ELSE)
# Performance Category Program

# 1. Prompt user for Input.
try:
    score = float(input("Enter your score (0 to 10): "))

    # Validate that the score is within the specified range
    if 0 <= score <= 10:
        
        # 2. Find the performance category based on the criteria
        if score > 7:
            category = "Above Average"
            message = "Excellent work! Keep up the great performance."
        elif score >= 4:  # Since we already checked > 7, this covers 4 to 7 inclusive
            category = "Average"
            message = "Good effort! Keep practicing, there's room for improvement."
        else:             # This covers anything less than 4
            category = "Below Average"
            message = "Need to improve your performance, consistent practice will lead to better results."
        
        # 3 & 4. Print the Performance category along with the additional prompt
        print(f"{category}: {message}")
        
    else:
        print("Invalid score. Please enter a number between 0 and 10.")

except ValueError:
    print("Invalid input. Please enter a numerical value.")
    