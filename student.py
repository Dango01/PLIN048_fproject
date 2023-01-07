class Student:
  
  def __init__(self, id, username, password, firstname, lastname):
    self.id = id
    self.username = username
    self.password = password
    self.firstname = firstname
    self.lastname = lastname
    self.enrolled_lessons = []

  def enroll_to_lesson(self, lesson):
    self.enrolled_lessons.append(lesson)
    lesson.enrolled_students.append(self)

  