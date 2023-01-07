from student import Student
from manager_service import ManagerService

class StudentService(ManagerService):
  
  def __init__(self):
    super().__init__()
    self.logged_user = None

  def username_exist(self, username):
    for student in self.db:
      if student.username == username:
        return True
    return False

  def choose_username(self):
    need_un = True
    while need_un:
      un = input("Zadej uživatelské jméno: ")
      if self.username_exist(un):
        print("Uživatelské jméno již existuje!")
      else:
        need_un = False
    return un
  
  def check_password(self, password):
    return True
  
  def choose_password(self):
    need_password = True
    while need_password:
      password = input("Zadej heslo: ")
      if self.check_password(password):
        password2 = input("Zadejte heslo znovu: ")
        if password == password2:
          need_password = False
        else:
          print("Hesla se neshodují")
      else:
        print("Heslo nesplňuje požadavky")
    return password
  
  def get_user(self, username):
    for student in self.db:
      if student.username == username:
        return student
    return None
    
  def register(self):
    un = self.choose_username()
    fname = input("Zadejte jméno: ")
    lname = input("Zadejte příjmení: ")
    password = self.choose_password()
    id = self.generate_id()
    student = Student(id, un, password, fname, lname)
    self.db.append(student)

  def show_students(self):
    for student in self.db:
      print(student.id)
      print(student.username)
      print(student.password)
      print(student.firstname)
      print(student.lastname)
    
  def login(self, username, password):
    user = self.get_user(username)
    if user == None:
      print("Uživatel neexistuje!")
      return
    if user.password != password:
      print("Špatné heslo!")
      return
    self.logged_user = user

  def logout(self):
    self.logged_user = None

  def get_logged_user(self):
    return self.logged_user