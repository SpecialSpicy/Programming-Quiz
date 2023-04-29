from tkinter import *
from tkinter import messagebox #import messagebox library


def new_game():
    
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print('-------------------------')
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter A, B, C or D: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):
    
    if answer == guess:
        print("Correct Answer!! 🤩")
        return 1
    else:
        print("Wrong Answer!! 🤬")
        return 0

def display_score(correct_guesses, guesses):
    print('-------------------------')
    print("Results: ")
    print('-------------------------')
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    if score == 0:
        print("Your score is: " + str(score)+"% 😖")
        rows = 10000000000
        columns = 100000000
        symbol = "😫😩 🥺 😢 😭 🤬 😤 😠 😡🫥 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 "
        for i in range(rows):
            while True:
                for j in range(columns):
                    print(symbol, end="")
                print()
    elif score == 25:
        print("Your score is: " + str(score)+"% 🙁")
    elif score == 50:
        print("Your score is: " + str(score)+"% 😐")
    elif score == 75:
        print("Your score is: " + str(score)+"% 😌")
    elif score == 100:
        print("Your score is: " + str(score)+"% 😍🍆🍑")
        
def play_again():
    
    response = input("Do you want to play again? (yes or no): ").upper()
    
    if response == 'YES':
        return True
    else:
        return False

questions = {
    "Who created Python?: ": "A",
    "What language was Windows written in?:" : "B",
    "What kind of language is PHP?:" : "C",
    "Which of the following does Javascript lack?:" : "A",
}


options =  [["A. Guido van Rossum", "B. Brenden Eich", "C. James Goslin", "D. Bjarne Stroustrup"],
            ["A. C++", "B. C#", "C. C", "D. Carbon"],
            ["A. Scripting Language", "B. Object-Oriented", "C. General-Purpose", "D. Machine Language"],
            ["A. Lists", "B. Constructors", "C. Objects", "D. Arrays"]]


new_game()

while play_again():
    new_game()

print("Goodbye and Have fun with your infected PC :)))")