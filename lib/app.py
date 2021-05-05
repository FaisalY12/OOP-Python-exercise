from .api import fetch_repos
from .repository import Repository


class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

class CLI():
    ''' User interface '''
    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'\n{Format.BLUE}{Format.BOLD}Welcome to github repo tracker!{Format.CLEAR}\n')
        self._user_input = input(f'''\n{Format.BLUE}Please enter your github username \n{Format.CLEAR}''')
        fetch_repos(self._user_input)
        self.menu()

    def menu(self):
        for idx, repository in enumerate(Repository.all, start=1):
            print(f'{idx}. {repository.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'''\n{Format.BLUE}Which repo would you like see more info for?\n{Format.CLEAR}''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repository()
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def show_repository(self):
        repository = Repository.find_by_input(self._user_input)
        print(f'\n{Format.BLUE}{Format.BOLD}{repository.name}{Format.CLEAR}')
        print(f'\tDescription: {repository.description}')
        print(f'\tLanguage: {repository.language}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repository.all)

    @staticmethod
    def goodbye():
        print(f'\n{Format.BLUE}{Format.BOLD}May the North be with you.{Format.CLEAR}\n')

if __name__ == '__main__':
    app = CLI()