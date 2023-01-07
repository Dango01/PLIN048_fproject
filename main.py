from app import App

app = App()

finished = app.run()

if finished:
  print("Aplikace byla úspěšně ukončena")
else:
  print("V aplikaci došlo k chybě")

  
# Test funkčnosti

'''sdb.register()


sdb.show_students()

ldb.add_lesson()
ldb.add_lesson()
ldb.show_lessons()
lid = int(input("Zadej ID lekce, kterou chceš zapsat"))
lesson = ldb.get_lesson(lid)
u.enroll_to_lesson(lesson)

sdb.register()
log_un = input("Zadejte UN: ")
log_pass = input("Zadejte Heslo: ")
sdb.login(log_un, log_pass)

▼
▼

ldb.add_lesson()
lesson = ldb.find_by_id(1)
task = lesson.tasks[0]
u = sdb.get_logged_user()
sub = subdb.submit_task(task, u)
subdb.evaluate_task(task, sub)

for task in lesson.tasks:
  print(task.id)
  print(task.question)
  for option in task.options:
    print(option.text)
  print()
for lesson in u.enrolled_lessons:
  print(lesson.name)
  
if u == None:
  print("FAIL")
else:
  print(u.id)

sdb.logout()
'''