
import json
import os

my_file= "students.json"
students=[]

# להוסיף קליטת ציון ע"פ מקצוע ולודא שאפשר לעשות את זה רק לסטונדט קיים
# אפשרות לחפש בגליון הציונים ע"פ סטונדט
# להוסיף תפריט ראשי האם אני רוצה להיכנס לסטונדטים או לגיליון הציונים

def display_gmenu():
    print('a -add')
    print("s - search")
    print("p - print all")
    print("x - exit")  

def display_mmenu(): # תפריטי משנה של לחפש סטודנט או להסויף ציון למקצוע ספציפי
    print("s - students")
    print("g - grades")
    print("x - exit") 


def display_stuMenu():
    print("a - add")
    print("s - search")
    print("p - print all")
    print("x - exit") 


def add_student():
    Sname =input('student name?')
    Email =input('student email?')
    students.append({"name":Sname,"email":Email})
    print('a student added')

def print_all():
    for student in students:
        print(student)

def add_to_file(): #כזה גם לציונים ולתפריט ראשי
    json_object = json.dumps(students, indent=4)
    print(json_object)
    with open(my_file, "w") as outfile:
	    outfile.write(json_object)

def load_from_stuFile():
    global students
    isExist = os.path.exists(my_file)
    if isExist:
        with open(my_file, 'r') as openfile:
            students = json.load(openfile)
        print(students)

def search():
    student_search=input('student name?')
    elmt = [x for x in students if x["name"] == student_search][0]
    if elmt:
        print(elmt)
        return True
    return False


def main():
    proMain = ''
    while (proMain != 'x'):
        if proMain == 's' : sinput
        if proMain == 'g' : ginput
        display_mmenu()
        stuInput=input()

        sinput = ''
        load_from_stuFile()

        while (stuInput  != 'x'):
            if stuInput == 's':
                if search() : 
                    print("Found")
                else:
                    print("not Found")          
            if stuInput == 'a':
                add_student()
            if stuInput == 'p':
                print_all()
            display_stuMenu()
            stuInput=input("what to do ?")
        add_to_file()

        ginput = ''
    


if __name__ == '__main__':
    main()
    




