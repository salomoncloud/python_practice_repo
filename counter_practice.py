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
    'id' : 123456789,   
}
queue ={
'Gcapacity':50,
'Rcapacity':40,
'Scapacity':30,
}


def GeorgeH():
    while True:
        checkin = int(input("Enter the number of patient : "))
        result = queue['Gcapacity'] + checkin
        if result < queue['Gcapacity']:
            print("Your waiting time is 3 Hours")
        else:
            result > queue['Gcapacity'] 
            print("Your waiting time is 6 Hours")
            return query
        

def RegisH():
    checkin = int(input("Enter the number of patient : "))
    result = queue['Rcapacity'] + checkin
    if result < queue['Rcapacity']:
        print("Your waiting time is 2 Hours")
    else:
        result > queue['Rcapacity'] 
        print("Your waiting time is 5 Hours")
        return query
    
    

def SalomonH():
    checkin = int(input("Enter the number of patient : "))
    result = queue['Scapacity'] + checkin
    if result < queue['Scapacity']:
        print("Your waiting time is 4 Hours")
    else:
        result > queue['Scapacity'] 
        print("Your waiting time is 7 Hours")
        return query
     
     
is_quit = False

print('')

print("Welcome to the Hospital System Queue")
resoan = str(input('Symptoms:'))
fname = str(input('Please enter your first name: '))
lname = str(input('Please enter your last name: '))
dob = int(input('Please enter your date of birth: '))
id = int(input('Please enter your Insurance Number: '))



if id ==  user['id']:
    while is_quit == False:
        print(" George Hospital Enter 1\n Regis Hospital Enter 2 \n Salomon Hospital Enter 3 \n Logout 4")

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
            print("Please enter a correct value ")
else:
    print("Please verify the information entered")