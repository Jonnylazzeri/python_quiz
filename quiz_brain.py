class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.score = 0
        self.q_list = q_list

    def still_has_questions(self):
        if self.q_num < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):

        while self.still_has_questions():
            text = self.q_list[self.q_num].q_text
            answer = self.q_list[self.q_num].q_answer
            self.q_num += 1
            guess = input(f'Q.{self.q_num}: {text} (True\False): ')
            if answer.lower() == guess.lower():
                self.score += 1
                print(f'Correct! Your current score is {self.score}/{self.q_num} questions right.')
            elif guess == 'exit':
                break
            else:
                print(f'Wrong! Your current score is {self.score}/{self.q_num} questions right.')

        else:
            print(f"You've completed the quiz. \nYour final score was {self.score}/{len(self.q_list)}")