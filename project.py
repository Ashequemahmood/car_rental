from datetime import datetime

# Menu
def menu():
    print("\nYou may select one of the following:")
    print("1) List available cars")
    print("2) Rent a car")
    print("3) Return a car")
    print("4) Count the money")
    print("5) Exit")
    operation = input("What is your selection?\n")
    return operation


def list_available_cars(file_name):
    print("The following cars are available:")
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    
    for line in lines:
        data = line.strip().split(",")
        print(f"* Reg. nr: {data[0]}, Model: {data[1]}, Price per day: {data[2]}")
        properties = data[3:]
        print("Properties:", end=" ")
    
        index = 0
        while index < len(properties):
            if index < len(properties) - 1:
                print(properties[index], end=", ")
            else:
                print(properties[index])  # Last property without trailing comma
            index += 1
    
    
def has_number(input_string):
    for char in input_string:
        if char.isdigit():
            return True
    return False


    

def check_if_returning_customer(birthday, file_name = "customers.txt"):
    f3 = open(file_name, "r")
    f3_data = f3.readlines()
    f3.close()
    
    for line in f3_data:
        if birthday in line:
            return True
    return False

def rent_car(file_name1, file_name2, file_name3):
    reg_nr = input("Give the register number of the car you want to rent:\n")
    
    f1 = open(file_name1, "r")
    f1_data = f1.readlines()
    f1.close()
    
    f2 = open(file_name2, "r")
    f2_data = f2.readlines()
    f2.close()
    
    car_exist = False
    for line1 in f1_data:
        if reg_nr in line1:
            car_exist = True
            break
        
    rented = False    
    if car_exist:
        for line2 in f2_data:
            if reg_nr in line2:
                rented = True
                break
    else:
        print("Car does not exist")
        return
        
    if rented:
        print(f"{reg_nr} already rented")
    else:
        while(True):
            birth_date = input("Please enter your birthday in the form DD/MM/YYYY:\n")
            # check if returning customer
            returning_customer = check_if_returning_customer(birth_date)
            
            
            try:
                
                now = datetime.now().date()
                date_format = "%d/%m/%Y"
                date_string1 = datetime.strptime(birth_date, date_format).date()
                
                age = now - date_string1
                min_age = 18*365
                max_age = 75*365
                
                if(age.days < min_age):
                    print("You are too young to rent a car, sorry!")
                    
                elif(age.days > max_age):
                    print("You are too old to rent a car, sorry!")
                    
                elif(returning_customer):
                    f3 = open(file_name3, "r")
                    f3_data = f3.readlines()
                    f3.close()
    
                    for line in f3_data:
                        if birth_date in line:
                            data = line.strip().split(",")                          
                            print("Age OK")
                            print(f"Hello {data[1]}")
                            print(f"You rented the car {reg_nr}")
                    # 2. rentedVehicles.txt append reg_nr, date, time:
                            now = datetime.now()
                            formatted_date = now.strftime("%d/%m/%Y %H:%M")
                            file2 = open(file_name2, "a")
                            data2 = file2.write(f"{reg_nr},{birth_date},{formatted_date}" + "\n")
                            file2.close()
                else:
                    print("Age OK")
                    while(True):
                        print("Names contain only letters and start with capital letters.")
                        first_name = input("Enter the first name of the customer:\n")
                        last_name = input("Enter the last name of the customer:\n")
                        # Check name first letter is uppercase and has no number in it:
                        num_in_first_name = has_number(first_name)
                        num_in_last_name = has_number(last_name)
                        
                        if(first_name[0].isupper() and last_name[0].isupper() and not num_in_first_name and not num_in_last_name):
                            while(True):
                                email = input("Give your email:\n")
                            # Check if valid email:
                                if not "@" in email:
                                    print("Give a valid email address")
                                elif not email[-4:] in ".com.org.edu.edu.net.lut":
                                    print("Give a valid email address")
                                else:
                                    break
                            
                            print(f"Hello {first_name}")
                            print(f"You rented the car {reg_nr}")
                            
                            # 1. customers.txt append date, name and email:
                            file1 = open(file_name3, "a")
                            data1 = file1.write(f"{birth_date},{first_name},{last_name},{email}" + "\n")
                            file1.close()
                            # 2. rentedVehicles.txt append reg_nr, date, time:
                            now = datetime.now()
                            formatted_date = now.strftime("%d/%m/%Y %H:%M")
                            file2 = open(file_name2, "a")
                            data2 = file2.write(f"{reg_nr},{birth_date},{formatted_date}" + "\n")
                            file2.close()
                            
                            break
                
                break
            except ValueError:
                print("There is not such date. Try again!")
        
def return_car(file_name1, file_name2):
        reg_nr = input("Give the register number of the car you want to return:\n")
        f1 = open(file_name1, "r")
        f1_data = f1.readlines()
        f1.close()
        
        for vehicle in f1_data:
            if reg_nr in vehicle:
                price_per_day = vehicle.split(",")[2]
        
    
        f2 = open(file_name2, "r")
        f2_data = f2.readlines()
        f2.close()
        
        for rented_v in f2_data:
            if reg_nr in rented_v:
                rent_day = rented_v.split(",")[2]
    
        car_exist = False
        for line1 in f1_data:
            if reg_nr in line1:
                car_exist = True
                break
        
        rented = False    
        if car_exist:
            for line2 in f2_data:
                if reg_nr in line2:
                    
                    rented = True
                    break
        else:
            print("Car does not exist")
            return
        
        if not rented:
            print("Car is not rented")
        else:
            date_format = "%d/%m/%Y"
            date_string1 = datetime.strptime(rent_day.split(" ")[0], date_format).date()
            now = datetime.now().date()
            period = now-date_string1
            cost = int(period.days) * int(price_per_day)
            print(f"The rent lasted {period.days} days and the cost is {round(cost, 2)} euros")
            # vehicle remove from rentedVehicles.txt file here
            file = open(file_name2, "r")
            lines = file.readlines()
            file.close()
            list = []
            for line in lines:
                if reg_nr not in line:
                    list.append(line)
            
            rented_v_file = open(file_name2, "w")
            rented_v_file.writelines(list)
            rented_v_file.close()
            
def count_money(file_name):
    
    file = open(file_name, "r")
    lines = file.readlines()
    file.close()
    sum = 0
    list = []
    for line in lines:
        data = line.strip().split(",")[5]
        list.append(data)
        
    for price in list:
        sum = sum + float(price)
        
    print(f"The total amount of money is {sum:.2f} euros")

def main():
    while(True):
        operation = menu()
        if(operation == "1"):
            list_available_cars(file_name = "vehicles.txt")
        elif(operation == "2"):
            rent_car(file_name1 = "vehicles.txt", file_name2 = "rentedVehicles.txt", file_name3 = "customers.txt")
        elif(operation == "3"):
            return_car(file_name1 = "vehicles.txt", file_name2 = "rentedVehicles.txt")
        elif(operation == "4"):
            count_money(file_name = "transActions.txt")
        elif(operation == "0"):
            print("Bye!")
            break
        else:
            continue

main()
