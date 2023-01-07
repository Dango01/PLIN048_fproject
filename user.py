class User:
  
  def __init__(self, id, username, password, firstname, lastname, paragraphs_entered, reviews_entered):
    self.id = id
    self.username = username
    self.password = password
    self.firstname = firstname
    self.lastname = lastname
    self.paragraphs_entered = []
    self.reviews_entered = []

  def assign_to_paragraph(self, paragraph):
    self.paragraphs_entered.append(paragraph)
    paragraph.who_entered.append(self)

  def assign_to_review(self, review):
    self.reviews_entered.append(review)
    review.who_reviewed.append(self)
  