from lesson import Lesson
from task_service import TaskService
from manager_service import ManagerService


class LessonService(ManagerService):

  def __init__(self):
    super().__init__()
    self.task_service = TaskService()

  def show_lessons(self):
    for lesson in self.db:
      print(lesson.id)
      print(lesson.name)
      print()

  def add_lesson(self):
    name = input("Zadejte název lekce: ")
    description = input("Zadejte popis lekce: ")
    id = self.generate_id()
    lesson = Lesson(id, name, description)
    self.add_tasks(lesson)
    self.db.append(lesson)

  def add_tasks(self, lesson):
    print("Zadejte úlohy")
    want_to_add = True
    while want_to_add == True:
      task = self.task_service.add_task(lesson)
      lesson.add_task(task)
      want_to_add = self.yes_no_question("Chcete přidat další otázku? y/n ")
