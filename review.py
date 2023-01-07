class Review:

  def __init__(self, id, rated_paragraph, review_status, who_rated, timestamp):
    self.id = id
    self.rated_paragraph = rated_paragraph
    self.review_status = review_status
    self.who_rated = who_rated
    self.timestamp = timestamp
    # self.options = [] # probably no need for this here, figure out later (if I use it must add options back to the __init__ parenthesis)

  # probably no need for this here, figure out later
  # def add_option(self, option):
    # self.options.append(option)

  # MUST ADD:
  # a function that will add a timestamp to the self.timestamp
  