class User:
    def __init__(self, id, name, access_level):
        self.__id = id
        self.__name = name
        self.__access_level = access_level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):

    def __init__(self, id, name, access_level='admin'):
        super().__init__(id, name, access_level)
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, user_id):
        for i, user in enumerate(self.__users):
            if user.get_id() == user_id:
                del self.__users[i]
                return

        print(f"Пользователь с ID {user_id} не найден.")

    def get_users(self):
        return self.__users