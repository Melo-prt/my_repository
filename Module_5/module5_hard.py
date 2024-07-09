class User:
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(str(password))
        self.age = age


class Video:
    def __init__(self, title, duration):
        self.title = str(title)
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False


class UrTube:
    users = []  # Список пользователей
    videos = []  # Список видео
    current_user = ''  # Текущий пользователь

    def log_in(self, login, password):
        for user in self.users:
            if user.nickname == login and user.password == hash(password):
                self.current_user = user
                return
            else:
                'Неверный логин или пароль'
                return
            

    def register(self, nickname, password, age):
        if nickname in self.users.keys():
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users[nickname] = hash(password)
        self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        if video in self.videos:
            print('Видео с таким названием уже существует')
        else:
            self.videos.append(video)

    def get_videos(self, word):
        self.word = word.lower
        for i in self.videos:
            if self.word in self.videos:
                print(self.videos[i])
            else:
                break


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10)

ur.add(v1, v2)
print(ur.videos)

print(ur.get_videos('Лучший'))
print(ur.get_videos('ПРОГ'))

# ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# ur.watch_video('Лучший язык программирования 2024 года!')
