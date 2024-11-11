from datetime import datetime

now = datetime.now()

print(now)


formated_date1 = now.strftime("%d/%m/%Y")
print(formated_date1)

name = input("Enter name:\n")
file = open("write.txt", "a")
data = file.write(f"{formated_date1}, {name}" + "\n")
file.close()