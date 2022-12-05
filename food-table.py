# this scripy was written by trapzzy, it is mean to help diabeties patiences with the chocies of food too eat each day for a better healthly livivng!!
print("{+}========{+} DAILY FOOD MENU FOR DIABETES PATIENTS{+}======{+}")
print("  ")
import  time
time.sleep(3)
print("INSTRUCTIONS: hey this would help you make a better choice!!")

class_of_food = (
"Carbohydrates",
"Fat and oil",
"Protein",
"Vitamins",
"Mineral",
"Water"
)
today = str(input("What day is it today?: "))
def day_of_the_week():
    global  today
    name = str(input("Enter your Full-name: "))
    print("  ")
    #today = str(input("What day is it today?: "))

    if today == 'monday':
        print(f'[+]For monday: ' + '{0[0]}'.format(class_of_food))

    elif today == 'tuesday':
        print(f'[+]For tuesday: ' + '{0[1]}'.format(class_of_food))

    elif today == 'wednesday':
        print(f'[+]For wednesday: ' + '{0[2]}'.format(class_of_food))

    elif today == 'thursday':
        print(f'[+]For thursday: ' + '{0[3]}'.format(class_of_food))

    elif today == 'friday':
        print(f'[+]For friday: ' + '{0[4]}'.format(class_of_food))

    elif today == 'saturday':
        print(f'[+]For saturday: ' + '{0[1]}'.format(class_of_food))

    elif today == 'sunday':
        print(f'[+]For sunday: ' + '{0[0:1]}'.format(class_of_food))

    else:
        print("WRONG INPUT!!")
        print("please type the correct days of the week for today!!....")

CONDITION = day_of_the_week()


print(CONDITION)

import classoffood as head

while True:
    if today == 'monday':
        print(head.day.monday(self= 'GOOD'))
        break
    elif today == 'tuesday':
            print(head.day.tuesday(self= 'GOOD'))
            break
    elif today == 'wednesday':
            print(head.day.wednesday(self= 'GOOD'))
            break
    elif today == 'thursday':
            print(head.day.thursday(self= 'GOOD'))
            break
    elif today == 'friday':
            print(head.day.friday(self= 'GOOD'))
            break
    elif today == 'saturday':
            print(head.day.saturday(self= 'GOOD'))
            break
    elif today == 'sunday':
            print(head.day.sunday(self= 'GOOD'))
            break
    else:
        print("WRONG INPUT!!")
        break


