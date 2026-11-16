import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read student data
data = pd.read_csv("students.csv", header=None)

data.columns = ["Name", "Maths", "Physics", "Chemistry"]

# Check invalid marks
subjects = ["Maths", "Physics", "Chemistry"]

for sub in subjects:
    data[sub] = pd.to_numeric(data[sub], errors="coerce")

data = data.dropna()

data = data[
    (data[subjects] >= 0).all(axis=1) &
    (data[subjects] <= 100).all(axis=1)
]

if data.empty:
    print("No valid student data found.")

else:
    # Calculate total and percentage
    data["Total"] = data[subjects].sum(axis=1)
    data["Percentage"] = data["Total"] / 3

    # Calculate grades
    def grade(p):
        if p >= 90:
            return "A"
        elif p >= 75:
            return "B"
        elif p >= 60:
            return "C"
        elif p >= 40:
            return "D"
        else:
            return "F"

    data["Grade"] = data["Percentage"].apply(grade)

    # Menu
    print("\n1. Show Student Results")
    print("2. Show Class Statistics")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nStudent Results:")
        print(data[["Name", "Total", "Percentage", "Grade"]])

    elif choice == "2":

        marks = data[subjects].values.flatten()

        print("\nClass Statistics")

        print("Mean:", np.mean(marks))
        print("Median:", np.median(marks))
        print("Standard Deviation:", np.std(marks))

        # Find topper
        topper = data.loc[data["Percentage"].idxmax()]

        print("Topper:", topper["Name"])

        # Subject average
        print("\nSubject Average:")
        print(data[subjects].mean())

        # Bar chart
        data[subjects].mean().plot(kind="bar")

        plt.title("Subject Wise Average")
        plt.xlabel("Subjects")
        plt.ylabel("Average Marks")
        plt.show()

        # Histogram
        plt.hist(marks, bins=5, edgecolor="black")

        plt.title("Student Marks Distribution")
        plt.xlabel("Marks")
        plt.ylabel("Students")
        plt.show()

    else:
        print("Invalid Choice")