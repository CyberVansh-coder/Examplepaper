import time
import os

# --------------------------
# Banner 1 Function
# --------------------------
def print_banner():
    print("""
 __         ______     ______     __     __   __    
/\ \       /\  __ \   /\  ___\   /\ \   /\ "-.\ \   
\ \ \____  \ \ \/\ \  \ \ \__ \  \ \ \  \ \ \-.  \  
 \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_\\"\_\ 
  \/_____/   \/_____/   \/_____/   \/_/   \/_/ \/_/ 
""")

# --------------------------
# Registration Function
# --------------------------
def register():
    print("\n🔐 User Registration")
    username = input("Enter a new student Id: ")
    password = input("Enter a new password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("✅ Registration Successful!\n")


# --------------------------
# Login Function
# --------------------------
def login():
    print("🔑 User Login")
    username = input("Enter Your Student Id: ")
    password = input("Enter Your Password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            u, p = user.strip().split(",")
            if u == username and p == password:
                print(f"✅ Welcome, {username}! Start Your Quiz\n")
                return True
    print("❌ Invalid credentials! Try again.\n")
    return False

# --------------------------
# Banner 2 (Direct print)
# --------------------------
print("""
    [....                        
  [..    [..          [.         
[..       [..[..  [..   [.... [..
[..       [..[..  [..[..     [.. 
[..       [..[..  [..[..   [..   
  [.. [. [.. [..  [..[..  [..    
    [.. ..     [..[..[..[........
         [.                       
""")

# --------------------------
# Ask a Question
# --------------------------
def ask_question(question, options, correct_ans):
    global Quiz, Score
    print(f"\nQues {Quiz + 1}. {question}\n")
    for i, opt in enumerate(options, 1):
        print(f"{i}\t {opt}")
    try:
        ans = int(input("Choose Your Correct Answer: "))
        if ans == correct_ans:
            print("✅ Right Answer.......")
            Score += 1
        else:
            print("❌ Wrong Answer!.......")
    except:
        print("⚠️ Invalid Input! Treated as wrong.")
    Quiz += 1

# --------------------------
# Loading Animation
# --------------------------
def loading():
    print("\nPlease wait", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\nAlmost Done...")
    time.sleep(2)

# --------------------------
# Questions List
# --------------------------
questions = [
    ("What is the shortcut key to create a new folder?",
     ["Ctrl + N", "Ctrl + Shift + N", "Alt + F4", "Shift + F2"], 2),

    ("What is the use of 'Folder Options'?",
     ["To Rename Folder", "Hide/Unhide Folders", "To Delete Files", "To Open Paint"], 2),

    ("What is stored in the Recycle Bin?",
     ["Saved Files", "Deleted Files and Folders", "Installed Software", "Printer Drivers"], 2),

    ("When a file is restored from the Recycle Bin, where does it go?",
     ["Downloads", "Desktop", "Original Location", "My Computer"], 3),

    ("What can be adjusted in Mouse Properties?",
     ["Change Wallpaper", "Change Mouse Pointer Speed", "Change Monitor Resolution", "Printer Settings"], 2),

    ("Which mouse button opens the shortcut (context) menu?",
     ["Left Click", "Double Click", "Right Click", "Scroll Button"], 3),

    ("Where is the taskbar located?",
     ["At the Top of the Screen", "In the Center of the Desktop", "At the Bottom of the Screen", "Inside Windows Explorer"], 3),

    ("What is shown on the taskbar?",
     ["Wallpaper", "Task Manager", "Start Button, Clock, and Open Apps", "BIOS Settings"], 3),

    ("What type of files can be edited in Notepad?",
     [".doc", ".xls", ".ppt", ".txt"], 4),

    ("What is a quick way to open Notepad?",
     ["Type \"notepad\" in Run", "Open Paint", "Link It From MS Word", "Use Task Manager"], 1),
]

# --------------------------
# Main Program
# --------------------------
print_banner()

# Register/Login Choice
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        register()
    elif choice == "2":
        if login():
            break
    elif choice == "3":
        exit()
    else:
        print("Invalid choice.\n")

# Quiz Start
Quiz = 0
Score = 0

for q in questions:
    ask_question(q[0], q[1], q[2])

loading()

# Show Final Result
print("\n🎯 Quiz Finished!")
print("Total Questions =", Quiz)
print("Total Score =", Score)

percentage = (Score / Quiz) * 100
print("Percentage =", percentage, "%")

# Grade System Based on Percentage
if percentage >= 90:
    print("🌟 Excellent! You're a computer wizard!")
elif percentage >= 75:
    print("👍 Very Good! Keep it up!")
elif percentage >= 50:
    print("🙂 Good. But you can do better!")
elif percentage >= 30:
    print("😐 Needs Improvement. Study more!")
else:
    print("❌ Fail. Don't give up, try again!")
