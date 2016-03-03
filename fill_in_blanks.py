print "This is the Fill in the Blanks Python Quiz!"
print "Good Luck!"

num_of_blanks = ["blank1", "blank2", "blank3", "blank4"]

#These are the levels for the quiz
easy_question= """ Bob ____1____ wrote Blowing in the Wind; He was friends John Lennon of The ____2____. He also recorded a song with Johnny ____3____ who sang Folsom Prison Blues. He also sang the song Like a Rolling___4____."""
medium_question= """Romeo ____2_____ fell in love with _____2_____ Capulet. Her cousin _____3_____ killed Romeo's friend _____4______."""
hard_question= """Doubt thou the ____1____ are fire, Doubt that the ____2_____ doth move; Doubt _____3_____ to be a liar; But never doubt I ____4_____."""

#These are the answers
easy_answers= ["Dylan", "Lennon", "Cash", "Stone"]
medium_answers= ["Montague", "Juliet", "Tybalt", "Mercutio"]
hard_answers= ["Stars", "Sun", "Truth", "Love"]

#This will  deter the level of difficulty for each question
def question_level():
    difficulty = raw_input("Choose the difficulty of your quiz!")
    if difficulty == "easy":
        return easy_question
    elif difficulty == "medium":
        return medium_question 
    elif difficulty == "hard"
        return hard_question
    else:
        print "That is not a level."
print question_level()

def answer_level():
    if difficulty == "easy":
        answers = easy_answers
        return = answers
    if difficulty == "medium":
        answers = medium_answers
        return answers
    else:
        answers = hard_answers
        return answers

#This will allow user to take the quiz
def take_quiz(num_of_blank):
    index = 0
    blank_string, answers = question_level()
    for answer in answers:
            user_input= raw_input("The answer is: " + answer + " ")
            while index < len(answer):
                if user_input == answer.index(answer):
                    return "Correct!"
                    index = index+1
                else:
                    return "Please Try Again."
        print blank_string
        take_quiz()
