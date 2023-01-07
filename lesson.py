class Lesson:

  def __init__(self, id, name, description):
    self.id = id
    self.name = name
    self.description = description
    self.enrolled_students = []
    self.tasks = []

  def add_task(self, task):
    self.tasks.append(task)