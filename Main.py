"""Integration Project"""

__author__ = "Sam Weiss"


class Question:
    """This implements the class 'Question'."""
    # implementing constructor
    def __init__(self, question, p_answer1, p_answer2, p_answer3, p_answer4, answer):
        self.question = question
        self.p_answer1 = p_answer1
        self.p_answer2 = p_answer2
        self.p_answer3 = p_answer3
        self.p_answer4 = p_answer4
        self.answer = answer

    # method to display the question
    def displayQuestion(self):
        """This function displays the questions."""
        print(self.question)
        print(self.p_answer1)
        print(self.p_answer2)
        print(self.p_answer3)
        print(self.p_answer4)


def quiz():
    """This function is what the quiz game uses to run."""
    # creating question objects
    q1 = Question("A group of cats are called?", "1. A clowder", "2. A pace",
                  "3. A troop", "4. A pack", 1)
    q2 = Question("A group of sharks are called?", "1. A murder", "2. A flock",
                  "3. A shiver ", "4. An army ", 3)
    q3 = Question("A group of giraffe are called?", "1. A battery ",
                  "2. A pack ", "3. A herd ", "4. A tower ", 4)
    q4 = Question("A group of dogs are called?", "1. A brood ", "2. A pack ",
                  "3. A troop ", "4. A sleuth ", 2)
    q5 = Question("A group of clams are called?", "1. A pod ", "2. A mob ",
                  "3. A bed ", "4. A cast ", 2)
    q6 = Question("A group of bears are called?", "1. A sleuth ", "2. A gang ",
                  "3. A trip ", "4. A band ", 1)
    q7 = Question("A group of crows are called?", "1. A cast ", "2. A pack ",
                  "3. A tribe ", "4. A murder ", 4)
    q8 = Question("A group of lions are called?", "1. A pack ", "2. A pride ",
                  "3. A troop ", "4. A romp ", 2)
    q9 = Question("A group of whales are called?", "1. A party ", "2. A team ",
                  "3. A pod ", "4. A herd ", 3)
    q10 = Question("A group of otters are called?", "1. A romp ", "2. A troop",
                   "3. A pack ", "4. A leap ", 1)

    # for player 1 and 2
    flag = 0

    player1_score = 0
    player2_score = 0

    # list of questions
    question_bank = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    print("******* Welcome to the Quiz Game! *******\n")

    for question in question_bank:
        if flag == 0:
            print("Its Player 1's turn:")
            print("-------------------------")

            # displaying question
            question.displayQuestion()

            answer = input("Enter your answer (1 or 2 or 3 or 4):")
            answer = int(answer)

            # checking wrong or right
            if question.answer == answer:
                print("-------------------------")
                print("Right answer!")
                print("-------------------------")
                player1_score += 1
            else:
                print("-------------------------")
                print("Wrong answer!")
                print("-------------------------")
            flag = 1
        else:
            print("Its Player 2's turn:")
            print("-------------------------")

            # displaying question
            question.displayQuestion()

            answer = input("Enter your answer (1 or 2 or 3 or 4):")
            answer = int(answer)

            # checking wrong or right
            if question.answer == answer:
                print("-------------------------")
                print("Right answer!")
                print("-------------------------")
                player2_score += 1
            else:
                print("-------------------------")
                print("Wrong answer!")
                print("-------------------------")
            flag = 0

    # printing up scores of players
    print("Player 1 | score:" + str(player1_score))
    print("Player 2 | score:" + str(player2_score))
    print("-------------------------")

    # printing up the results
    if player1_score > player2_score:
        print("Player 1 wins the game!")
        print("-------------------------")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
        print("-------------------------")
    else:
        print("It's a tie...")
        print("-------------------------")


# main menu
def menu():
    """This function prints the menu, which is the first thing the user sees
    when running the program."""
    print("-------Main Menu------")
    print("1. Quiz Game")
    print("2. Tip and Tax calculator")
    print("0. Exit")
    print("-------------------------")

    option = input("Choose option : ")

    return option


# calculating tip
def calc_tip(mealprice):
    """This function calculates the price of a tip based on the price of the
    meal."""
    tip = mealprice * .15

    return tip


# calculating tax
def calc_tax(mealprice):
    """This function calculates how much is taxed on top of the original
    meal price."""
    tax = mealprice * .06

    return tax


# calculating total
def calc_total(mealprice, tip, tax):
    """This function calculates the total of all the values used in the
    tip calculator."""
    total = mealprice + tip + tax

    return total


# printing the whole information
def print_info(mealprice, tip, tax, total):
    """This function is used to print all the values used in the tip
    calculator."""
    print("The meal price is $", mealprice)

    print("The tip is $", round(tip))

    print("The tax is $", round(tax))
    print("-------------------------")
    print("The total is $", round(total))
    print("-------------------------\n")


# getting meal price from user
def getMealPrice():
    """This function is used to determine the price of the meal, which the
    user inputs."""
    mealprice = input("Enter the meal price $")
    mealprice = float(mealprice)

    return mealprice


# Main method
def main():
    """This function is the main function, in which all the other functions
    run."""
    print("Welcome to my Integration Project!")
    while True:
        option = menu()
        print("-------------------------")

        if option == "1":
            # starting the quiz
            quiz()
        elif option == "2":
            # calculating tip and tax

            # calling methods for calculations
            mealprice = getMealPrice()

            tip = calc_tip(mealprice)

            tax = calc_tax(mealprice)

            total = calc_total(mealprice, tip, tax)

            # printing the information
            print_info(mealprice, tip, tax, total)

        elif option == "0":
            # ending up the program
            print("You have exited the program.")
            break


# calling main method
if __name__ == '__main__':
    main()
