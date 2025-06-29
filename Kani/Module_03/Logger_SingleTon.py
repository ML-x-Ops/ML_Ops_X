class Logger:

    _login = None

    def __new__(cls):
        if cls._login == None:
            cls._login = super().__new__(cls)
            print(f"New user login at this address {cls._login}")
        return cls._login
    
    def log_in(cls):
        print("You have logged in successfully")

pubg_game = Logger()

ff_game = Logger()

print(pubg_game is ff_game)

pubg_game.log_in()

ff_game.log_in()