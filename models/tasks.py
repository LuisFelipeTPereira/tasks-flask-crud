class Task:
    def __init__(self, id, title, description, complete=False):
        self.id = id
        self.title = title
        self.description = description
        self.complete = complete
        
    def to_dict(self):
        return  {
            "id": self.id,
            "title": self.title,
            "description":self.description,
            "complete":self.complete
        }