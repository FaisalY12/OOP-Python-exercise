class Repository():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._description = data['description']
        self._language = data['language']
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def description(self):
        return self._description

    @property
    def language(self):
        return self._language
    
    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]