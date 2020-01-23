class User:
    
    user_round = None

    def __init__(self, chat_info) -> None:
        self.id = chat_info.id
        self.username = getattr(chat_info, 'username', 'Anonymous')
        self.first_name = getattr(chat_info, 'first_name', 'Anonymous')
        self.last_name = getattr(chat_info, 'last_name', 'Anonymous')