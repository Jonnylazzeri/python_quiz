# class User:
#     def __init__(self, user_id, username):
#
#         self.user_id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
# user_1 = User('001', 'jonny')
# user_2 = User('002', 'Meir')
#
# user_1.follow(user_2)
#
# print(user_1.following)
# print(user_2.followers)

import html

from question_data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_list = []

for question in question_data:
    question_list.append(Question(html.unescape(question["question"]), question["correct_answer"]))

quiz = QuizBrain(question_list)
quiz.next_question()
