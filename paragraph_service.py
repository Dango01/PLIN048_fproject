from user_service import UserService
from paragraph import Paragraph
from task_service import TaskService
from manager_service import ManagerService


class ParagraphService(ManagerService):

  def __init__(self):
    super().__init__()
    self.task_service = TaskService()
    self.id_list = []
    self.author_list = []
    self.chapter_list = []
    self.page_list = []
    self.publisher_list = []
    self.language_list = []
    self.entered_by_list = []
    self.review_status_list = []

  def show_paragraphs(self):
    for paragraph in self.db:
      print('\n[PARAGRAPH_LIST]')
      print(f"ID: {paragraph.id}")
      self.id_list.append(paragraph.id)
      print(f"Author: {paragraph.author}")
      self.author_list.append(paragraph.author)
      print(f"Chapter: {paragraph.chapter}")
      self.chapter_list.append(paragraph.chapter)
      print(f"Page: {paragraph.page}")
      self.page_list.append(paragraph.page)
      print(f"Publisher: {paragraph.publisher}")
      self.publisher_list.append(paragraph.publisher)
      print(f"Language: {paragraph.language}")
      self.language_list.append(paragraph.language)
      print(f"Entered by: {paragraph.entered_by}")
      self.entered_by_list.append(paragraph.entered_by)
      print(f"Review status: {paragraph.review_status}")
      self.review_status.append(paragraph.review_status)

  def add_paragraph(self):
    want_to_add = True
    while want_to_add == True:
      id = self.generate_id()
      author = input("Zadajte meno autora: ")
      chapter = input("Zadajte názov kapitoly: ")
      page = input("Zadajte stranu: ")
      publisher = input("Zadajte názov vydavateľa: ")
      language = input("Zadajte jazyk paragrafu: ")
      entered_by = UserService.log_u
      review_status = "not reviewed"
      paragraph = Paragraph(id, author, chapter, page, publisher, language, entered_by, review_status)
      self.db.append(paragraph)
      want_to_add = self.yes_no_question("Chcete pridať ďalší paragraf? y/n ")
       
#  self.add_tasks(paragraph)

  #def add_tasks(self, lesson):
  #  print("Zadejte úlohy")
  #  want_to_add = True
  #  while want_to_add == True:
  #    task = self.task_service.add_task(lesson)
  #    lesson.add_task(task)
  #    want_to_add = self.yes_no_question("Chcete přidat další otázku? y/n ")
