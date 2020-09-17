from colorama import Fore,Style
class Question:
    def __init__(self,question,answer):
        self.question=question
        self.answer=answer

    #to start the quiz, we need to display questions and check for the answers

    def start(self):
        score=0
        for q in range(len(self.question)):
            print(self.question[q])
            ans=input(Fore.YELLOW+"your answer->  "+Style.RESET_ALL)
            print('---------------')
            if ans==self.answer[q]:
                score+=1
        print(".......... END OF THE QUIZ ..........\n")
        print(f"you have answered {score}/{len(self.question)} correctly!")