import csv
import os
import random
# Ensure the current working directory is set to the desired path
New_directory = "c:/Users/bjayd/OneDrive/Desktop/ChampionPicker"
os.chdir(New_directory)
print(os.getcwd())
        #print("Current working directory:", os.getcwd())
        #print("Files in the directory:", os.listdir())
print("Welcome to the Champion Picker!")
print("This program will randomly select a champion for you to play in League of Legends based on the role you select.")
print("Pick one of the following: Top, Jungle, Mid, Bot, Support")
Role = input("What Role are you play?: ")

# Count the number of rows in the CSV file
Champions = "ChampionList.csv"
num_rows = 0
with open('ChampionList.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        num_rows += 1

# filters based on the selected role
if num_rows > 0:
    with open('ChampionList.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        filtered_champions = [row for row in reader if row[2].strip().lower() == Role.strip().lower()]

#take the filtered champions and creates a csv file with the champions that match the role
    with open('FilteredChampions.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        writer.writerows(filtered_champions)

#reads the filtered champions from the CSV file and selects a random champion
    with open('FilteredChampions.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        filtered_champions = [row for row in reader]

# Select a random index from the filtered list and -1 for the header
print(f"Number of champions available for {Role}: {len(filtered_champions)}")


print(f"Randomly selected champion Champion: {random.choice(filtered_champions)[0]}")

#deletes the filtered champions CSV file
os.remove('FilteredChampions.csv')
print("FilteredChampions.csv has been deleted.")

#keeps the command prompt open until the user presses enter
input("Press Enter to exit the program...")
