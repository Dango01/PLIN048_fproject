from submission import Submission
from manager_service import ManagerService

class SubmissionService(ManagerService):

  def __init__(self):
    super().__init__()

  def select_options(self, task):
    selected_options = []
    for option in task.options:
      answer = self.yes_no_question(option.text + " - Chcete zaškrtnout? y/n ")
      if answer:
        selected_options.append(option)
    return selected_options
  
  def submit_task(self, task, user):
    print(task.question)
    for option in task.options:
      print(option.text)
    print("Zadejte svou odpověď")
    selected_options = self.select_options(task)
    submission = Submission(task, user, selected_options)
    self.db.append(submission)
    return submission

  def evaluate_task(self, task, submission):
    correct = 0
    for option in task.options:
      if option in submission.answer:
        print("X " + option.text)
      else:
        print(" " + option.text)
      if (option.correct == True and option in submission.answer) or (option.correct == False and option not in submission.answer):
        print("Správně")
        correct+=1
      else:
        print("Špatně")
    print("Body: " + str(task.points * correct/len(task.options)))
        