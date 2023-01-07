from task import Task
from option import Option
from manager_service import ManagerService

class TaskService(ManagerService):

  def __init__(self):
    super().__init__()
    
  def add_options(self, task):
    print("Zadejte možnosti")
    want_to_add = True
    while want_to_add == True:
      option = self.new_option(task)
      task.add_option(option)
      want_to_add = self.yes_no_question("Chcete přidat další možnost? y/n ")
      
    
  def new_option(self, task):
    text = input("Zadejte text možnosti: ")
    correct = self.yes_no_question("Má být možnost zaškrtnutá? y/n ")
    option = Option(text, correct, task)
    return option
        
  def add_task(self, lesson):
    question = input("Zadej otázku: ")
    points = int(input("Zadej počet bodů: "))
    id = self.generate_id()
    new_task = Task(id, question, points, lesson)
    self.add_options(new_task)   
    self.db.append(new_task);
    return new_task
  