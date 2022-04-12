from Import_code import LinkedList

LOOP = True

class Song:
    def __init__(self, song, artist, year):
        self.__song = song
        self.__artist = artist
        self.__year = year

    def getSong(self):
        song = self.__song
        return (song)

    def getArtist(self):
        artist = self.__artist
        return (artist)

    def getYear(self):
        year = self.__year
        return (year)

def save(song_list):
    with open("song_list.txt", 'w') as opened_file:
        opened_file.write("Song,Artist,Year\n")
        for song in song_list:
            opened_file.write(f"{song.getSong()},{song.getArtist()},{song.getYear()}\n")

def play_from_song(song_list):
    user_input = str(input("Enter the song to start\n:"))
    head_value = song_list.getHead()
    
    while(True):
        if head_value.element.getSong() == user_input:
            break
        head_value = head_value.next
    
    while(True):
        print(f"{head_value.element.getSong()} {head_value.element.getArtist()} {head_value.element.getYear()}")
        head_value = head_value.next
        if head_value == None:
            return

def delete_song(song_list):
    user_input = str(input("Enter the name of the song\n:"))
    index = 0
    for song in song_list:
        if user_input == song.getSong():
            removed_song = song_list.removeAt(index)
            break
        index += 1
    print(f"{removed_song.getSong()} is deleted")

def add_song(song_list):
    user_input = str(input("Enter the song in this format: Song,Artist,Year\n:"))
    song_artist_year = user_input.split(',')
    song = Song(song_artist_year[0],song_artist_year[1],song_artist_year[2])
    song_list.add(song)
    print("Song Added")

def user_start(song_list):
    user_input = str(input("""\nMusic play simulator\nA. Play all \nB. Add a song\nC. Delete a song\nD. Start playing from a song\nE: Exit\n:"""))
    if user_input == 'A':
        print("Playing")
        for song in song_list:
            print(f"{song.getSong()} {song.getArtist()} {song.getYear()}")
    if user_input == 'B':
        add_song(song_list)
    if user_input == 'C':
        delete_song(song_list)
    if user_input == 'D':
        play_from_song(song_list)
    if user_input == 'E':
        save(song_list)
        global LOOP
        LOOP = False

def main():
    song_list = LinkedList()
    
    with open("song_list.txt", 'r') as opened_file:
        file = opened_file.read().splitlines()
        for line in file:
            if line[0:16] == "Song,Artist,Year":
                continue
            song_artist_year = line.split(',')
            song = Song(song_artist_year[0],song_artist_year[1],song_artist_year[2])
            song_list.add(song)
    while LOOP:
        user_start(song_list)
           
main()