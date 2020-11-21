ARTIST_NAME = 0
ALBUM_NAME = 1
RELEASE_YEAR = 2
GENRE = 3
LENGTH = 4


def get_albums_by_genre(albums, genre):
    """
    Get albums by genre

    :param list albums: albums' data
    :param str genre: genre to filter by

    :returns: all albums of given genre
    :rtype: list
    """
    albums_genres = list(set([album[GENRE] for album in albums]))
    if genre not in albums_genres:
        raise ValueError("Wrong genre")
    specific_genre_albums = [album for album in albums if album[GENRE] == genre]
    return specific_genre_albums

def get_genre_stats(albums):
    """
    Get albums' statistics showing how many albums are in each genre
    Example: { 'pop': 2, 'hard rock': 3, 'folk': 20, 'rock': 42 }

    :param list albums: albums' data
    :returns: genre stats
    :rtype: dict
    """

    albums_genres = list([album[GENRE] for album in albums])
    number_of_albums = dict.fromkeys(albums_genres)
    for genre in albums_genres:
        if number_of_albums[genre] is None:
            number_of_albums[genre] = 1
        else:
            number_of_albums[genre] += 1
    return number_of_albums


def get_longest_album(albums):
    """
    Get album with biggest value in length field.
    If there are more than one such album return the first (by original lists' order)

    :param list albums: albums' data
    :returns: longest album
    :rtype: list
    """
    longest_album_value = max([float(album[LENGTH].replace(":", ".")) for album in albums])
    for index, album in enumerate(albums):
        if float(album[LENGTH].replace(":", ".")) == longest_album_value:
            return albums[index]

def get_last_oldest(albums):
    """
    Get last album with earliest release year.
    If there is more than one album with earliest release year return the last
    one of them (by original list's order)

    :param list albums: albums' data
    :returns: last oldest album
    :rtype: list
    """
    oldest = 2020
    index_oldest = 0
    for index, album in enumerate(albums):
        if int(album[RELEASE_YEAR]) <= oldest:
            oldest = int(album[RELEASE_YEAR])
            index_oldest = index
    return albums[index_oldest]


def get_last_oldest_of_genre(albums, genre):
    """
    Get last album with earliest release year in given genre

    :param list albums: albums' data
    :param str genre: genre to filter albums by
    :returns: last oldest album in genre
    :rtype: list
    """
    albums_genres = list([album for album in albums if album[GENRE] == genre])
    return get_last_oldest(albums_genres)

def to_time(str):
    """
    converts time in format "minutes:seconds" (string) to seconds (int)
    """
    #int(album[LENGTH])

def get_total_albums_length(albums):
    """
    Get sum of lengths of all albums in minutes, rounded to 2 decimal places
    Example: 3:51 + 5:20 = 9.18             
             231 + 320 seconds = 551 seconds

    :param list albums: albums' data
    :returns: total albums' length in minutes
    :rtype: float
    """
    # albums_length = [float(album[LENGTH].replace(":", ".")[3:])/60 for album in albums]
    albums_length = []
    for album in albums:
        album = album[LENGTH].split(":")
        album_minutes = float(album[0])
        album_seconds = float(album[1])/60
        album_length = album_minutes + album_seconds
        albums_length.append(album_length)
        total_length = sum(albums_length)
    return round(total_length, 2)