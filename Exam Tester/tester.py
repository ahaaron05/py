import random

class Quizzer:
    """A simple Exam Quiz study machine"""

    def __init__(self):
        self.questions = [
            "What are some big recording companies in the early 1900s?: ",
            "Explain the phonographs invention and creator?: ",
            "Explain the parts of the phonograph?: ",
            "How did early recording work in the early 1900s?: ",
            "Explain the invention of electrical recording?: ",
            "Explain home recording and its importance?: ",
            "Explain the adoption of tape recording by the music industry?: ",
            "What was special about Cleveland, Ohio?: ",
            "Explain the development of recording studios?: ",
            "Explain the significance of early trade magazines in home recordings?: "
            #"Talk about WWI era recording companies?: ",
            #"Talk about WWII era recording companies?: ",
            #"Explain the transition from wax cylinders in professional studios?: ",
            #"Talk about the invention of multi-track recording techniques?: ",
            #"What were some challenges that multi-tracking introduced?: ",
            #"What are the benefits of multitrack recording?: ",
            #"Explained multitrack jazz recording and the challenges with it?: ",
            #"Talk about the studio innovations of the Beatles and the Beach Boys in the 1960s?: ",
            #"Explain the transition to stereo recording?: ",
            #"Explain microphones and postware microphone improvements?: ",
            #"Talk about the Musician's strike of 1942-44?: ",
            #"Talk about the development of the LP record?: ",
            #"What is Strange Fruit?: ",
             ]
        self.answers = [
            "Gennett, Victor, and Columbia\n",
            "The phonograph was made initially by Martinville in 1857, but later realized and improved by Thomas Edison in 1877. It consisted of wax cylindars\n",
            "The sound was made on wax or foil cylinders. A horn to play into, a recording needle to scratch the cylinder, and a thin glass diaphram.\n",
            "You recorded in a lab and stood around a phonograph. It was accoustical and very dependent on positioning. Very secretive and difficult.\n",
            "Invented in Bell Labs by Maxwell, electric recording  transformed sound into electrical signals. This meant louder and more consisten sound. Also allowing for direct monitoring and levels.\n",
            "It allowed more people to experiment and try new teqniques in a more casual setting. Some people of note: Savory, Asch, Laico, Plunkett. Great depression was a big reason for its rise.\n",
            "The Brush BK was able to edit reuse and erase audio tapes. Allowed for overdubbing and taking more takes instead of needing to be perfect. This was the Ampex model.\n"
            "Was the birth of some great new studios for Polka and such. These include: Cleveland Records, Schneider, Grand Funke Railroad.\n",
            "Some became big and famous with lots of equipment, while others maintained a low but reliable profile, with quality over scale.\n",
            "The magazines helped to get the average person involved with music recording.\n"
            #""
           ]
    
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