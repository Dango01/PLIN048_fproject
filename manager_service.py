class ManagerService:

  def __init__(self):
    self.db = []

  def get_max_id(self):
    max_id = 0
    for item in self.db:
      if item.id >= max_id:
        max_id = item.id
    return max_id
  
  def generate_id(self):
    max_id = self.get_max_id()
    return max_id + 1

  def yes_no_question(self, question):
    while True:
      answer = input(question)
      if answer == "y":
        return True
      elif answer == "n":
        return False

  def find_by_id(self, id):
    for item in self.db:
      if id == item.id:
        return item
    return None