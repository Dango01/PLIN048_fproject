class Task:

  def __init__(self, id, question, points, lesson):
    self.id = id
    self.question = question
    self.points = points
    self.options = []
    self.lesson = lesson

  def add_option(self, option):
    self.options.append(option)
    