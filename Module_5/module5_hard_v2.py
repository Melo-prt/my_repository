import time


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self, title: str, duration: int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __contains__(self, item):
        return item in self.title

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname: str, password: str, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует.')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print('Вы успешно зарегистрированы!')

    def log_in(self, login, password):
        for user in self.users:
            if login == user.nickname and hash(password) == user.password:
                self.current_user = user.nickname

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for vid in video:
            if vid not in self.videos:
                self.videos.append(vid)

    def get_videos(self, word):
        word = word.lower()
        list_video = []
        for video in self.videos:
            if word in video.title.lower():
                list_video.append(video.title)
        return list_video

    def watch_video(self, name):
        if self.current_user is not None:
            for video in self.videos:
                if video.adult_mode == True and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    if name == video.title:
                        for i in range(1, video.duration):
                            print(i)
                            time.sleep(1)
                        print('Конец видео.')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео.')





ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')