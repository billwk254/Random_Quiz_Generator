import random
import os

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

#creates a new folder for putting in all our files in if it does not exist

if os.path.exists("C:\\Users\\billk\\Desktop\\us_state_capitals_quiz"):
    pass
else:
    os.makedirs("C:\\Users\\billk\\Desktop\\us_state_capitals_quiz\\question_sheets")
    os.makedirs("C:\\Users\\billk\\Desktop\\us_state_capitals_quiz\\answer_sheets")

for quiznum in range(35):
    # create the quiz and answer key files
    quizfile = open("C:\\Users\\billk\\Desktop\\us_state_capitals_quiz\\question_sheets\\capitalsquiz%s.txt" % (quiznum + 1), "w")
    answerkeyfile = open("C:\\Users\\billk\\Desktop\\us_state_capitals_quiz\\answer_sheets\\capitalsquiz_answers%s.txt" % (quiznum + 1), "w")

    #write out the header for the quiz
    quizfile.write("Name:\n\nDate:\n\nClass\n\n")
    quizfile.write(('' * 20) + "State Capitals quiz (Form %s)" % (quiznum + 1))
    quizfile.write("\n\n")

    #Shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    #get right and wrong answers
    for questionnum in range(50):
        correctanswer = capitals[states[questionnum]]
        wronganswer = list(capitals.values())
        del wronganswer[wronganswer.index(correctanswer)]
        wronganswer = random.sample(wronganswer, 3)
        answeroptions = wronganswer + [correctanswer]
        random.shuffle(answeroptions)

        #write the question and the answer options to the quiz file

        quizfile.write("%s.What is the capital of %s?\n" % (questionnum + 1, states[questionnum]))
        for i in range(4):
            quizfile.write("  %s.%s\n" % ("ABCD"[i], answeroptions[i]))
        quizfile.write("\n")

        #write the answer key to a file
        answerkeyfile.write("%s.%s\n" % (questionnum +1, "ABCD"[answeroptions.index(correctanswer)]))
    quizfile.close()
    answerkeyfile.close()




