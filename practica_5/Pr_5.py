import random


class Music:
    def __init__(self, title, genre, listens_last_week):
        self.title = title
        self.genre = genre
        self.listens_last_week = listens_last_week


class User:
    def __init__(self, first_name, last_name, middle_name, favorite_songs, genres, weekly_listens):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.favorite_songs = favorite_songs
        self.genres = genres
        self.weekly_listens = weekly_listens

    def get_max_listens_index(self):
        max_index = 0
        for i in range(1, len(self.weekly_listens)):
            if self.weekly_listens[i] > self.weekly_listens[max_index]:
                max_index = i
        return max_index


class Playlist:
    def __init__(self, full_name, recommended_songs):
        self.full_name = full_name
        self.recommended_songs = recommended_songs

    def has_genre_match(self, user, song):
        for genre in user.genres:
            if genre.lower() == song.genre.lower():
                return True
        return False


def main():
    music_library = []
    possible_titles = ["Song A", "Song B", "Song C", "Song D", "Song E",
                       "Song F", "Song G", "Song H", "Song I", "Song J"]
    possible_genres = ["Rock", "Pop", "Jazz", "Classical", "Hip-Hop"]

    for i in range(10):
        title = possible_titles[i]
        genre = random.choice(possible_genres)
        listens = random.randint(1, 100)
        music_library.append(Music(title, genre, listens))

    print("Введите имя:")
    first_name = input()
    print("Введите фамилию:")
    last_name = input()
    print("Введите отчество:")
    middle_name = input()

    fav_count = 5
    fav_songs = []
    user_genres = []
    user_listens = []

    print("Введите 5 избранных композиций и их жанры:")
    for i in range(fav_count):
        print(f"Название композиции {i + 1}:")
        song_name = input()
        fav_songs.append(song_name)
        print("Жанр:")
        genre = input()
        user_genres.append(genre)
        user_listens.append(random.randint(1, 50))

    user = User(first_name, last_name, middle_name, fav_songs, user_genres, user_listens)

    genre_total_listens = {}
    for i in range(len(user.genres)):
        genre = user.genres[i]
        listens = user.weekly_listens[i]
        if genre in genre_total_listens:
            genre_total_listens[genre] += listens
        else:
            genre_total_listens[genre] = listens

    favorite_genre = ""
    max_listens = -1
    for genre, total in genre_total_listens.items():
        if total > max_listens:
            max_listens = total
            favorite_genre = genre

    print(f"\nЛюбимый жанр пользователя: {favorite_genre} (прослушиваний: {max_listens})")

    recommendations = []

    for song in music_library:
        if song.genre.lower() == favorite_genre.lower():
            recommendations.append(f"{song.title} ({song.genre})")
        elif song.listens_last_week > max_listens * 1.5:
            recommendations.append(f"{song.title} ({song.genre}) [популярнее любимого жанра]")

    if not recommendations:
        print("\nНет совпадений по жанру. Рекомендуем самые прослушиваемые композиции:")
        music_library.sort(key=lambda x: x.listens_last_week, reverse=True)
        for i in range(min(5, len(music_library))):
            recommendations.append(
                f"{music_library[i].title} ({music_library[i].genre}) - {music_library[i].listens_last_week} прослушиваний")

    full_name = f"{last_name} {first_name} {middle_name}"
    playlist = Playlist(full_name, recommendations)

    print(f" ПОДБОРКА для {playlist.full_name} ")
    for rec in recommendations:
        print(f"- {rec}")

    print("\nОбновляем статистику прослушиваний:")
    print("После рекомендации, прослушивания песен увеличились на 10:")
    for song in music_library:
        for rec in recommendations:
            if rec.startswith(song.title):
                song.listens_last_week += 10
                print(f"  {song.title}: теперь {song.listens_last_week} прослушиваний ")


if __name__ == "__main__":
    main()