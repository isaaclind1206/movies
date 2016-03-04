print "This is the Fill in the Blanks Python Quiz!"
print "Good Luck!"

num_of_blanks = ["____1____", "____2____", "____3____", "____4____"]

#These are the levels for the quiz
easy_question= """ Bob ____1____ wrote Blowing in the Wind; He was friends John Lennon of The ____2____. He also recorded a song with Johnny ____3____ who sang Folsom Prison Blues. He also sang the song Like a Rolling____4____."""
medium_question= """Romeo ____1____ fell in love with ____2____ Capulet. Her cousin____3____ killed Romeo's friend ____4____."""
hard_question= """Doubt thou the ____1____ are fire, Doubt that the ____2____ doth move; Doubt ____3____ to be a liar; But never doubt I ____4____."""

#These are the answers
easy_answers= ["Dylan", "Lennon", "Cash", "Stone"]
medium_answers= ["Montague", "Juliet", "Tybalt", "Mercutio"]
hard_answers= ["Stars", "Sun", "Truth", "Love"]


#This will  deter the level of difficulty for each question
def question_level():
    difficulty = raw_input("Choose the difficulty of your quiz!")
    if difficulty == "easy":
        return easy_question, easy_answers
    elif difficulty == "medium":
        return medium_question, medium_answers 
    elif difficulty == "hard":
        return hard_question, hard_answers
    else:
        print "That is not a level."
        exit ()


#This will allow user to take the quiz
def take_quiz(num_of_blank):
    index = 0
    blank_string, answers = question_level()
    for index in range (len(answers)):
            user_input= raw_input("The answer is: " + answer + " ")
            while userInput != correctAnswer:
                prompt user again
                print "Correct!"
                blank_string = blank_string.replace(num_of_blanks[index], answers[index])
                    index = index+1
                else:
                    return "Please Try Again."
        print blank_string
take_quiz()
