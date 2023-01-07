from user import User
from manager_service import ManagerService

class UserService(ManagerService):
  
  def __init__(self):
    super().__init__()
    self.logged_user = None 

  def username_exist(self, username):
    for user in self.db:
      if user.username == username:
        return True
    return False

  def choose_username(self):
    need_un = True
    while need_un:
      un = input("Zadajte uživateľské meno: ")
      if self.username_exist(un):
        print("Uživateľské meno už existuje!")
      else:
        need_un = False
    return un
  
  def check_password(self, password):
    return True
  
  def choose_password(self):
    need_password = True
    while need_password:
      password = input("Zadajte heslo: ")
      if self.check_password(password):
        password2 = input("Zadajte heslo znova: ")
        if password == password2:
          need_password = False
        else:
          print("Heslá sa nezhodujú!")
      else:
        print("Heslo nespĺňa požiadavky!")
    return password
  
  def get_user(self, username):
    for user in self.db:
      if user.username == username:
        return user
    return None
    
  def register(self):
    un = self.choose_username()
    fname = input("Zadajte meno: ")
    lname = input("Zadajte priezvisko: ")
    password = self.choose_password()
    id = self.generate_id()
    paragraphs_entered = []
    reviews_entered = []
    user = User(id, un, password, fname, lname, paragraphs_entered, reviews_entered)
    self.db.append(user)

  def show_users(self):
    for user in self.db:
      print(user.id)
      print(user.username)
      print(user.password)
      print(user.firstname)
      print(user.lastname)

  log_u = ""
  
  def login(self, username, password):
    user = self.get_user(username)
    if user == None:
      print("Uživateľ neexistuje!")
      return
    if user.password != password:
      print("Nesprávne heslo!")
      return
    self.logged_user = user
    log_u = user.username
    return log_u
  
  def logout(self):
    self.logged_user = None

  def get_logged_user(self):
    return self.logged_user
