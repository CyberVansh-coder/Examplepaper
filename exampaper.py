Quiz = 0
Score = 0

print("Ques 1. What is the shortcut key to create a new folder?\n")
print("1\t Ctrl + N")
print("2\t Ctrl + Shift + N")
print("3\t Alt + F4")
print("4\t Shift + F2")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 2:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 2. What is the use of 'Folder Options'?\n")
print("1\t To Rename Folder")
print("2\t Hide/Unhide Folders")
print("3\t To Delete Files")
print("4\t To Open Paint")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 2:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 3. What is stored in the Recycle Bin?\n")
print("1\t Saved Files")
print("2\t Deleted Files and Folders")
print("3\t Installed Software")
print("4\t Printer Drivers")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 2:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 4. When a file is restored from the Recycle Bin, where does it go?\n")
print("1\t Downloads")
print("2\t Desktop")
print("3\t Original Location")
print("4\t My Computer")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 3:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 5. What can be adjusted in Mouse Properties?\n")
print("1\t Change Wallpaper")
print("2\t Change Mouse Pointer Speed")
print("3\t Change Monitor Resolution")
print("4\t Printer Settings")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 2:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 6. Which mouse button opens the shortcut (context) menu?\n")
print("1\t Left Click")
print("2\t Double Click")
print("3\t Right Click")
print("4\t Scroll Button")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 3:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 7. Where is the taskbar located?\n")
print("1\t At the Top of the Screen")
print("2\t In the Center of the Desktop")
print("3\t At the Bottom of the Screen")
print("4\t Inside Windows Explorer")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 3:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 8. What is shown on the taskbar?\n")
print("1\t Wallpaper")
print("2\t Task Manager")
print("3\t Start Button, Clock, and Open Apps")
print("4\t BIOS Settings")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 3:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 9. What type of files can be edited in Notepad?\n")
print("1\t .doc")
print("2\t .xls")
print("3\t .ppt")
print("4\t .txt")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 4:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

print("\nQues 10. What is a quick way to open Notepad?\n")
print("1\t Type \"notepad\" in Run")
print("2\t Open Paint")
print("3\t Link It From MS Word")
print("4\t Use Task Manager")
Quiz += 1
ans = int(input("Choose Your Correct Answer: "))
if ans == 1:
    print("Right Answer.......")
    Score += 1
else:
    print("Wrong Answer!.......")

import time
print("please wait.....")
time.sleep(10)
print("Almost Done.....")
time.sleep(5)
print("Total Questions =",Quiz)
print("Total Score =", Score)
