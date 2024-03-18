import random

class Quizzer:
    """A simple Exam Quiz study machine"""

    def __init__(self):
        with open("Exam Tester/questions.txt", 'r') as q_file:
            self.questions = q_file.readlines()
        with open("Exam Tester/answers.txt", 'r') as a_file:
            self.answers = a_file.readlines()

    def start_quiz(self):
        """Start the quiz"""

        print("\nWelcome to Aaron's Quizzzler.......Let's begin!\n")
        print("When you have answered the question, enter 'show' to show correct answer...\n")
        print("Press 'q' to quit\n")

        # ask user random question. Then enter 'show' to show answer
        while True:
            rand_index = random.randint(0, (len(self.questions)) - 1)
            chosen = self.questions[rand_index]
            user_input = input(chosen)
            if user_input.lower() == 'q':
                break
            elif user_input.lower() == 'show':
                print(f"\nCorrect Answer:\t{self.answers[rand_index]}\n")
                continue
            

quiz = Quizzer()
quiz.start_quiz()