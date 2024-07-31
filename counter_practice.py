# using looping, im gonna practice here a loop over an iterable list and sum up the total of the list

waiting_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in waiting_list:
    counter = counter + item

print(counter)

# loop runs code over and over after every value, so setting a counter variable outside the loop you can ensure that counter wont change after adding every piece of the list

# project practice --- creating a counter for our hospital that 

# Hospital Queue
user = {
    'id': 123456789,   
}

queue = {
    'Gcapacity': 45,
    'Rcapacity': 75,
    'Scapacity': 25,
}

# Counters for the current number of patients in each hospital
current_patients = {
    'George': 39,
    'Regis': 72,
    'Salomon': 5,
}

def GeorgeH():
    checkin = int(input("Enter the number of patients: "))
    if current_patients['George'] + checkin <= queue['Gcapacity']:
        current_patients['George'] += checkin
        print(f"Your position in the queue is: {current_patients['George']}")
        print("Your waiting time is 3 Hours")
    else:
        print("Hospital is at full capacity. Please wait or choose another hospital.")
    
def RegisH():
    checkin = int(input("Enter the number of patients: "))
    if current_patients['Regis'] + checkin <= queue['Rcapacity']:
        current_patients['Regis'] += checkin
        print(f"Your position in the queue is: {current_patients['Regis']}")
        print("Your waiting time is 2 Hours")
    else:
        print("Hospital is at full capacity. Please wait or choose another hospital.")
    
def SalomonH():
    checkin = int(input("Enter the number of patients: "))
    if current_patients['Salomon'] + checkin <= queue['Scapacity']:
        current_patients['Salomon'] += checkin
        print(f"Your position in the queue is: {current_patients['Salomon']}")
        print("Your waiting time is 4 Hours")
    else:
        print("Hospital is at full capacity. Please wait or choose another hospital.")

is_quit = False

print('')
print("Welcome to the Hospital System Queue")
symptoms = str(input('Symptoms: '))
fname = str(input('Please enter your first name: '))
lname = str(input('Please enter your last name: '))
dob = int(input('Please enter your date of birth: '))
id = int(input('Please enter your Insurance Number: '))

if id == user['id']:
    while not is_quit:
        print("\nGeorge Hospital Enter 1\nRegis Hospital Enter 2\nSalomon Hospital Enter 3\nLogout Enter 4")
        query = int(input("Please Choose a Hospital: "))

        if query == 1:
            GeorgeH()
        elif query == 2:
            RegisH()
        elif query == 3:
            SalomonH()
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value")
else:
    print("Please verify the information entered")
