#import all the required packages
import random
import os
from countries_and_capitals_generator import country_capitals
from generate_by_continents import continentselector
from generate_by_continents import country_capitals2
from generate_by_continents import delete_previous
import re

#a dictionary with states in the US and their state capitals
"""
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

"""
#regular expression to help in identifying when there are more quiz files than the number requested by the user
questionfileregex = re.compile(r"(capitalsquiz)(\d?\d)")
answerfileregex =  re.compile(r"(capitalsquiz_answers)(\d?\d)")

def num_of_students():
    """A function that asks the user to input how many students are being tested"""
    global studentnum
    while True:
        studentnum = int(input("How many students are you planning to test: \n"))
        if studentnum:
            break

num_of_students()

def userpath():
    """creates a new folder for putting in all our files in if it does not exist"""
    global questionfolder, answerfolder,userpath
    while True:
        userpath = os.path.abspath(input("Please enter a path to use to store the files: \n"))
        userpath = os.path.join(userpath,"world_capitals_quiz")
        if not os.path.exists(userpath):
            questionfolder = os.path.join(userpath,"question_sheets\\")
            answerfolder = os.path.join(userpath,"answer_sheets\\")
            os.makedirs(questionfolder)
            os.makedirs(answerfolder)
            break
        elif os.path.exists(userpath):
            break
        else:
            continue

userpath()

#lists for storing all the excess files in the question and answer folders
excessquestionfiles = []
excessanswerfiles = []

def quiz_type():
    """a function which lets the user select a specific continent to draw the quiz from or generate a quiz with all countries"""
    while True:
        global capitals
        user_select =  input("Do you want to generate a quiz for a specific continent(C) or for all countries(A): \n")
        if user_select:
            if user_select.lower() == "c":
                continentselector()
                capitals = country_capitals2
                break
            elif user_select.lower() == "a":
                capitals = country_capitals
                break
            else:
                continue

quiz_type()


for quiznum in range(studentnum):
    # create the quiz and answer key files
    quizfile = open(f"{userpath}\\question_sheets\\capitalsquiz%s.txt" % (quiznum + 1), "w")
    answerkeyfile = open(f"{userpath}\\answer_sheets\\capitalsquiz_answers%s.txt" % (quiznum + 1), "w")

    #write out the header for the quiz
    quizfile.write("Name:\n\nDate:\n\nClass\n\n")
    quizfile.write(('' * 20) + "Capitals quiz (Form %s)" % (quiznum + 1))
    quizfile.write("\n\n")

    #Shuffle the order of the states
    countries = list(capitals.keys())
    random.shuffle(countries)

    #get right and wrong answers
    for questionnum in range(0,len(capitals)):
        correctanswer = capitals[countries[questionnum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroptions = wronganswer + [correctanswer]
        random.shuffle(answeroptions)

        #write the question and the answer options to the quiz file

        quizfile.write("%s.What is the capital of %s?\n" % (questionnum + 1, countries[questionnum]))
        for i in range(4):
            quizfile.write("  %s.%s\n" % ("ABCD"[i], answeroptions[i]))
        quizfile.write("\n")

        #write the answer key to a file
        answerkeyfile.write("%s.%s\n" % (questionnum +1, "ABCD"[answeroptions.index(correctanswer)]))
    quizfile.close()
    answerkeyfile.close()

def delete_overflow():
    """function to delete all excess files found in the folders where the quiz and its answer files are being generated
    from previous runs of the program"""

    for files in os.listdir(f"{userpath}\\question_sheets"):
        if files.endswith(".txt"):
            exquestions = questionfileregex.search(files)
            if int(exquestions.group(2)) > studentnum:
                excessquestionfiles.append(files)
    for ofiles in os.listdir(f"{userpath}\\answer_sheets\\"):
        if files.endswith(".txt"):
            exanswers = answerfileregex.search(ofiles)
            if int(exanswers.group(2)) > studentnum:
                excessanswerfiles.append(ofiles)
    for exq in excessquestionfiles:
        delfilelocation = os.path.join(f"{userpath}\\question_sheets", exq)
        os.remove(delfilelocation)
    for exa in excessanswerfiles:
        delfilelocation2 = os.path.join(f"{userpath}\\answer_sheets\\", exa)
        os.remove(delfilelocation2)

delete_overflow()

def check_location_numbering():
    """A function that uses a regular expression to check the last location that the program
    output the test files to"""
    global locnumber, previouslocation, recheck,beforedir
    recheck = re.compile(r"^(\d\d?\d?)(\W)(.*)$")
    checkfolder = open("world_capitals_quiz.txt","r")
    checkfiles = checkfolder.read()
    flist = checkfiles.split("\n")
    required = flist[-2]
    numsearch = recheck.search(required)
    if numsearch:
        locnumber = int(numsearch.group(1))
    else:
        locnumber = 0
    beforedir = numsearch.group(3)
    checkfolder.close()

check_location_numbering()

def delete_last_folder_location():
    """A function that asks the user to delete the last location the program output
    the test files to if the user happens to change output locations"""
    if len(os.listdir(f"{userpath}\\question_sheets")) == studentnum:
        global folderpath
        folderpath = os.path.abspath(f"{userpath}")
        folderlocation = open(f"{os.path.basename(folderpath)}.txt","a")
        count = locnumber
        while True:
            folderlocation.write("%s. %s\n"%(count + 1, folderpath))
            break
        folderlocation.close()
        checkfolder = open("world_capitals_quiz.txt", "r")
        checkfiles = checkfolder.read()
        flist = checkfiles.split("\n")
        required = flist[-2]
        numsearch = recheck.search(required)
        afterdir = numsearch.group(3)
        if beforedir != afterdir:
            while True:
                deleteprompt = input(f"Do you want to delete the folder generated in the location {beforedir}(Y/N): \n")
                if deleteprompt.lower() == "y":
                    delete_previous(beforedir)
                    print(f"The Folder {beforedir} has been permanently deleted")
                    break
                elif deleteprompt.lower() == "n":
                    print("KEEPING THINGS IN THE SAME DIRECTORY I SEE, VERY SMART!")
                    break
                else:
                    print("Please Enter Yes(Y) or No(N)")
                    continue
        else:
            print("{0:>50}".format("KEEPING THINGS IN THE SAME DIRECTORY AVOIDS CONFUSION AND DECLUTTERS YOUR COMPUTER"))
        checkfolder.close()



delete_last_folder_location()

print("THE TEST AND ANSWER FILES FOR " + str(studentnum) + f" STUDENTS HAS BEEN STORED TO THE FOLLOWING LOCATION \n\n ********{userpath}********* ")




