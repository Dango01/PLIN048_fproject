class Paragraph:

  def __init__(self, id, author, chapter, page, publisher, language, entered_by, review_status):
    self.id = id
    self.author = author
    self.chapter = chapter
    self.page = page
    self.publisher = publisher
    self.language = language
    self.entered_by = entered_by
    self.review_status = review_status
    # self.options = [] # probably no need for this here, figure out later (if I use it must add options back to the __init__ parenthesis)
    
  # probably no need for this here, figure out later
  # def add_option(self, option): 
    # self.options.append(option)

  # MUST ADD:
  # a function/or redefine the review_status so it is recorded here from review class 
    # for example: self.review_status = review.review_status ?
