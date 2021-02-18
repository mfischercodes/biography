''' Ask user for their info one question at a time.
Then check if the information is valid.
Finally print a summary of all the information given  '''
import re

questions_directory = ["Name","Date of birth","Address", "Personl goals"]

def questions(questions_dirc = questions_directory):
    users_answers = [input(f"What is your {questions}? ")for questions in questions_dirc]

    def validate():
        for i in range(len(questions_dirc)):
            if (questions_dirc[i] == "Name"):
                if len(users_answers[i]) < 3:
                    print("Please input a name with more than 2 characters.")
                    return "Error"
            if (questions_dirc[i] == "Date of birth"):
                if not (re.search(r"\d", users_answers[i])):
                    print("No digits were input please input a proper date of birth.")
                    return "Error"     

    if (validate() == "Error"): return
    validate()

    def bibliography():
        for question in range(len(questions_dirc)):
            print(f"{questions_dirc[question]}: {users_answers[question]}")
            
    bibliography()

questions()

