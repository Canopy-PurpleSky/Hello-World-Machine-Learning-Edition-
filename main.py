import random

class Question:
    def __init__(self,options=list,correct = int):
        self.options = options
        self.correct = correct

    def ask(self):
        ask_resp = input("Correct: ")

        trial = self.options.count(ask_resp)
        print(trial)

        if trial > 0 :
            pass
        elif trial < 0 :
            pass

Powerpoint = Question([1,2,3],3)
Powerpoint.ask()
