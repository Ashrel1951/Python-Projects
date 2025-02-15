class Player:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = 0

    def greet(self):
        print("Welcome!")
        if self.gender.lower() == "male":
            print("Welcome Sir")
        elif self.gender.lower() == "female":
            print("Welcome Madam")
        else:
            print("Welcome!")


class QuizGame:
    def __init__(self):
        # Initialize questions and choices
        self.questions = {
            "Who developed the Python Programming Language?": "c",
            "Which programming paradigms does Python support?": "d",
            "Which among these is the correct extension for a Python file?": "c",
            "Is Python a compiled or interpreted language?": "a",
            "Which symbol is used for single-line comments?": "b"
        }

        self.choices = [
            ["a) Wick van Rossum", "b) Rasmus Lerdorf", "c) Guido van Rossum", "d) Nieve Storm"],
            ["a) Object-oriented Programming", "b) Structured Programming", "c) Functional Programming", "d) All of the mentioned"],
            ["a) .python", "b) .pl", "c) .py", "d) .p"],
            ["a) Both compiled and interpreted", "b) Neither compiled nor interpreted", "c) Only compiled", "d) Only interpreted"],
            ["a) //", "b) #", "c) !", "d) /*"]
        ]

    def start_game(self, player):
        print("Let's start the game!\n")
        for i, (question, correct_answer) in enumerate(self.questions.items()):
            print(f"Question {i + 1}: {question}")
            for option in self.choices[i]:
                print(option)
            user_answer = input("Your answer (a/b/c/d): ").lower()
            if user_answer == correct_answer:
                print("Correct!")
                player.score += 1
            else:
                print("Incorrect!")

        print(f"\n{player.name}, your final score is: {player.score}/{len(self.questions)}")


def main():
    # Get player information
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")

    # Create Player instance
    player = Player(name, age, gender)
    player.greet()

    # Start Quiz Game
    game = QuizGame()
    game.start_game(player)


# Run the main function
if __name__ == "__main__":
    main()
