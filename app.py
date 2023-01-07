# import všetkých použitých tried
from user_service import UserService
from paragraph_service import ParagraphService
from task_service import TaskService
from submission_service import SubmissionService
import pandas as pd
import numpy as np

# táto trieda spúšťa celý program do chodu
class App:

  # tu treba privolať všetky triedy ktoré trieda App využíva a definovať úvodný stav
  def __init__(self):
    self.udb = UserService()
    self.pdb = ParagraphService()
    self.tdb = TaskService()
    self.subdb = SubmissionService()
    self.state = "auth"

  # univerzálne použíteľná yes/no question
  def yes_no_question(self, question):
    while True:
      answer = input(question)
      if answer == "y":
        return True
      elif answer == "n":
        return False

  # spustenie programu, načíta preddefinovaný úvodný stav a spustí aplikáciu   
  def run(self):
    while True:
      if self.state == "auth":
        self.show_auth()
      elif self.state == "menu":
        self.show_menu()
      elif self.state == "exit":
        return True
      else:
        return False

  # (úvodné) autentifikačné menu - voľba medzi prihlásením/registráciou/ukončením programu
  def show_auth(self):
    user = self.udb.get_logged_user()
    logout = False
    if user != None:
      logout = self.yes_no_question("Už ste prihlásený, chcete sa odhlásiť? y/n")
      if logout:
        self.udb.logout()
    else:
      print("1 Prihlásiť sa")
      print("2 Registrovať sa")
      print("3 Ukončiť aplikáciu")
      operation = int(input("Zvoľte operáciu: "))
      if operation == 1:
        username = input("Zadajte uživatelské meno: ")
        password = input("Zadajte heslo: ")
        self.udb.login(username, password)
        if self.udb.get_logged_user() != None:
          self.state = "menu"
      elif operation == 2:
        self.udb.register()
      elif operation == 3:
        self.state = "exit"
      else:
        print("Neznáma operácia")

  # (nasledujúce) akciové menu - voľba medzi vložením paragrafu, či hodnotenia
  def show_menu(self):
      print("1 Vložiť paragraf")
      print("2 Vložiť hodnotenie")
      print("3 Ukončiť aplikáciu")
      operation = int(input("Zvoľte operaciu: "))
      if operation == 1:
        self.pdb.add_paragraph()
        self.pdb.show_paragraphs()
        array = np.array(
          [pdb.id_list, pdb.author_list, pdb.chapter_list, pdb.page_list, pdb.publisher_list, pdb.language_list, pdb.entered_by_list, pdb.review_status_list])
        data = np.transpose(array, axes = None)
        df = pd.DataFrame(data, columns=["id", "first_name", "last_name", "username", "password"])
        print(f'''\n[USER_DATABASE]
        {df}\n''')
      elif operation == 2:
        self.sdb.register()
      elif operation == 3:
        self.state = "exit"
      else:
        print("Neznáma operácia")