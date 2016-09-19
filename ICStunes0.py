##
## ICStunes:  A Music Manager
##
## Original version ("InfxTunes") in Scheme by Alex Thornton,
##      modified 2007 and 2008 by David G. Kay
## Python version by David G. Kay, 2012

from collections import namedtuple
#######################################
# Album, Song
#######################################

Album = namedtuple('Album', 'id artist title year songs')
# id is a unique ID number; artist and title are strings; year is a number,
#   the year the song was released; songs is a list of Songs

Song = namedtuple('Song', 'track title length play_count')
# track is the track number; title is a string; length is the number of
#   seconds long the song is; play_count is the number of times the user
#   has listened to the song

MUSIC = [
    Album(1, "Peter Gabriel", "Up", 2002,
        [Song(1, "Darkness", 411, 5),
         Song(2, "Growing Up", 453, 5),
         Song(3, "Sky Blue", 397, 2),
         Song(4, "No Way Out", 473, 2),
         Song(5, "I Grieve", 444, 2),
         Song(6, "The Barry Williams Show", 735, 1),
         Song(7, "My Head Sounds Like That", 389, 1),
         Song(8, "More Than This", 362, 1),
         Song(9, "Signal to Noise", 456, 2),
         Song(10, "The Drop", 179, 1)]),
    Album(2, "Simple Minds", "Once Upon a Time", 1985,
        [Song(1, "Once Upon a Time", 345, 9),
         Song(2, "All the Things She Said", 256, 10),
         Song(3, "Ghost Dancing", 285, 7),
         Song(4, "Alive and Kicking", 326, 26),
         Song(5, "Oh Jungleland", 314, 13),
         Song(6, "I Wish You Were Here", 282, 12),
         Song(7, "Sanctify Yourself", 297, 7),
         Song(8, "Come a Long Way", 307, 5)]),
    Album(3, "The Postal Service", "Give Up", 2003,
        [Song(1, "The District Sleeps Alone", 284, 13),
         Song(2, "Such Great Heights", 266, 13),
         Song(3, "Sleeping In", 261, 12),
         Song(4, "Nothing Better", 226, 18),
         Song(5, "Recycled Air", 269, 13),
         Song(6, "Clark Gable", 294, 12),
         Song(7, "We Will Become Silhouettes", 300, 11),
         Song(8, "This Place is a Prison", 234, 9),
         Song(9, "Brand New Colony", 252, 9),
         Song(10, "Natural Anthem", 307, 7)]),
    Album(4, "Midnight Oil", "Blue Sky Mining", 1989, #25225
        [Song(1, "Blue Sky Mine", 258, 12),
         Song(2, "Stars of Warburton", 294, 11),
         Song(3, "Bedlam Bridge", 266, 11),
         Song(4, "Forgotten Years", 266, 8),
         Song(5, "Mountains of Burma", 296, 9),
         Song(6, "King of the Mountain", 231, 8),
         Song(7, "River Runs Red", 322, 9),
         Song(8, "Shakers and Movers", 268, 9),
         Song(9, "One Country", 353, 7),
         Song(10, "Antarctica", 258, 6)]),
    Album(5, "The Rolling Stones", "Let It Bleed", 1969, #10569
        [Song(1, "Gimme Shelter", 272, 3),
         Song(2, "Love In Vain", 259, 2),
         Song(3, "Country Honk", 187, 0),
         Song(4, "Live With Me", 213, 2),
         Song(5, "Let It Bleed", 327, 2),
         Song(6, "Midnight Rambler", 412, 1),
         Song(7, "You Got the Silver", 170, 0),
         Song(8, "Monkey Man", 251, 13),
         Song(9, "You Can't Always Get What You Want", 448, 10)])
]
#######################################
# Sorting the collection
#######################################

# Sort the collection into chronological order
# The 'key=' argument of sort() takes a function---that function
#   takes an album and produces the value that will be used for
#   comparisons in the sort.
# So first we define that function

def Album_year(A: Album) -> int:
    ''' Return the album's year
    '''
    return A.year

MUSIC.sort(key=Album_year) # Oldest to newest
assert(MUSIC[0].title == "Let It Bleed") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Give Up")

MUSIC.sort(key=Album_year, reverse=True) # Newest to oldest
assert(MUSIC[0].title == "Give Up") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Let It Bleed")

# Sort the collection by Album title
def Album_title(A: Album) -> str:
    ''' Return the album's title
    '''
    return A.title

MUSIC.sort(key=Album_title)
assert(MUSIC[0].title == "Blue Sky Mining") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

# Sort the collection by length (playing time) of album
def Album_length(a: Album) -> int:
    ''' Return the total length of all the songs in the album
    '''
    total_length = 0
    for s in a.songs:
        total_length += s.length
    return total_length

MUSIC.sort(key=Album_length)
assert(MUSIC[0].title == "Once Upon a Time") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

# Sort the collection by Album id (as above)
def Album_id(A: Album) -> str:
    ''' Return the album's number
    '''
    return A.id

MUSIC.sort(key=Album_id)

## We can also write a conventional function to sort a collection, so
## we could say collection_sort(MUSIC, Album_length) instead of using
## the method notation MUSIC.sort(key=Album_length).  We do this by
## PASSING A FUNCTION AS A PARAMETER (like the interchangeable
## attachment on a robot arm).

def collection_sort(C: 'list of Album', keyfunction: 'Function on Albums') -> None:
    ''' Sort collection according to specified key function
        Note that this function, like the sort() method, sorts the collection
        IN PLACE (by reference), so it changes the argument it was called with.
        That's why it doesn't RETURN anything.
    '''
    C.sort(key=keyfunction)
    return

collection_sort(MUSIC, Album_title)
assert(MUSIC[0].title == "Blue Sky Mining") # Kind of a half-hearted test
assert(MUSIC[-1].title == "Up")

collection_sort(MUSIC, Album_id) # Just to put it back in the original order


#######################################
# Top 10 most frequently played songs
#######################################

# Collect all the songs out of all the albums.
# To find the MOST frequent, just use the find-largest (king-of-the-hill) algorithm
# To find the top N is hard to code that way.
# Better: Take the list of songs, sort by play_count, take first 10 -- songlist[:10]

def Song_play_count(s: Song) -> int:
    ''' Return the number of times this song has been played
    '''
    return s.play_count

def all_songs(MC: 'list of Album') -> 'list of Song':
    ''' Return a list of all the Songs in a music collection (list of Album)
    '''
    result = [ ]
    for a in MC:
        result.extend(a.songs)
    return result

Songlist = all_songs(MUSIC)
assert(Songlist[0] == Song(1, "Darkness", 411, 5))
assert(Songlist[1] == Song(2, "Growing Up", 453, 5))
assert(Songlist[-1] == Song(9, "You Can't Always Get What You Want", 448, 10))

def top_n_played_songs(MC: 'list of Album', n: int) -> 'list of Song':
    ''' Return a list of the n most frequently played songs in MC
    '''
    Songlist = all_songs(MC)
    Songlist.sort(key=Song_play_count, reverse=True)
    return Songlist[:n]

assert(top_n_played_songs(MUSIC, 5) ==
       [Song(4, "Alive and Kicking", 326, 26),
        Song(4, "Nothing Better", 226, 18),
        Song(5, "Oh Jungleland", 314, 13),
        Song(1, "The District Sleeps Alone", 284, 13),
        Song(2, "Such Great Heights", 266, 13)])


###################################
# Song-displays
###################################
# But these songs don't have their album information!  We removed it when we created
# the list of all songs.  If we want to display selected songs on our iPod screen,
# we'd want to have the album information along with the song information.

# We could flatten out our data structure, storing a copy of the album
# information with each song:
#       1   Up  Peter Gabriel  2002  1  Darkness   411   5
#       1   Up  Peter Gabriel  2002  2  Growing Up   453  8
#       1   Up  Peter Gabriel  2002  3  Sky Blue    397  2
#            ...
# This would work, but there's a lot of duplicate data---it would be wasteful of storage
# and error-prone to store our music data this way permanently.

# Instead, let's just get the album info that goes with a song WHEN WE NEED IT,
# during the computation.  To do this, we define a structure that contains the
# info we need to display a song (on our iPod screen, e.g.)---song details plus
# the info we need from that song's album:

Songdisplay = namedtuple('Songdisplay', 'artist a_title year track s_title length play_count')

# We'll create these structures as we need them during the computation,
# discarding them as we're done; this doesn't affect the main, permanent
# list of albums (like the one we defined as MUSIC above).

def all_Songdisplays(MC: 'list of Album') -> 'list of Songdisplay':
    ''' Return a list of all the songs in the collection MC, in Songdisplay form
    '''
    result = [ ]
    for a in MC:
        result.extend(Album_to_Songdisplays(a))
    return result

def Album_to_Songdisplays(a: Album) -> 'list of Songdisplay':
    ''' Return a list of Songdisplays, one for each song in the album
    '''
    result = [ ]
    for s in a.songs:
        result.append(Songdisplay(a.artist, a.title, a.year,
s.track, s.title, s.length, s.play_count))
    return result

def play_count_from_songdisplay(sd: Songdisplay) -> int:
    ''' Return the play_count from a Songdisplay
    '''
    return sd.play_count

def top_n_played(MC: 'list of Album', n: int) -> 'list of Songdisplay':
    ''' Return the top n most frequently played songs in MC
    '''
    list_of_Songdisplays = all_Songdisplays(MC)
    list_of_Songdisplays.sort(key=play_count_from_songdisplay, reverse=True)
    return list_of_Songdisplays[:n]

test_list = top_n_played(MUSIC, 3)
assert(test_list[0].s_title == "Alive and Kicking")
assert(test_list[0].a_title == "Once Upon a Time")
assert(test_list[-1].s_title == "Oh Jungleland")
assert(test_list[-1].a_title == "Once Upon a Time")

#
#E-1
#
song1 = Song(1, "Monkey Man", 251, 13)
def Song_str(s: Song) -> str:
    ''' Return a Song in string format
    '''
    return '{} {} {} {}'.format(s.track, s.title, s.length, s.play_count)
assert Song_str(song1) == '1 Monkey Man 251 13'

album1 = Album(1, "Peter Gabriel", "Up", 2002,
        [Song(1, "Darkness", 411, 5),
         Song(2, "Growing Up", 453, 5)])

def Album_str(a: Album) -> str:
    ''' Return an Album in string format
    '''
    string = '{} {} {} {}\n'.format(a.id, a.artist, a.title, a.year)
    for s in a.songs:
        string += '    '+Song_str(s)+'\n'
    return string
assert Album_str(album1) == \
'''1 Peter Gabriel Up 2002
    1 Darkness 411 5
    2 Growing Up 453 5
'''
def Collection_str(C: list) -> str:
    ''' Return a list of albums in string format
    '''
    string = ''
    for a in C:
        string += Album_str(a)
    return string


print('--------------E-1--------------\n ')
print('Album sorted by Album ID')
MUSIC.sort(key=Album_id)
print(Collection_str(MUSIC))
print('Album sorted by year\n')
MUSIC.sort(key=Album_year)
print(Collection_str(MUSIC))

songdisplay1 = Songdisplay('ABC', 'A1', 2014, 1, "Monkey Man", 251, 13)
def Songdisplay_str (sd: Songdisplay) -> str:
    ''' Return a songdisplay in string format
    ''' 
    return '{} -- {} -- {} -- {} -- {} -- {} -- {}'.format(sd.artist, sd.a_title, sd.year, sd.track, sd.s_title, sd.length, sd.play_count)     
assert Songdisplay_str(songdisplay1) == 'ABC -- A1 -- 2014 -- 1 -- Monkey Man -- 251 -- 13'
print('\nSongdisplay_str on test_list (test_list = top_n_played(MUSIC, 3))\n')
for songdisplay in test_list:
     print(Songdisplay_str(songdisplay))
#
# E-2
#
print('\n--------------E-2--------------\n ')
def Album_num_tracks(A: Album) -> int:
    '''return the number of trakcs in album'''
    return len(A.songs)
assert Album_num_tracks(album1) == 2
MUSIC.sort(key = Album_num_tracks)
print('Collection printed using Album_str after sorting MUSIC by Album_num_tracks\n')
for a in MUSIC:
    print(Album_str(a))
MUSIC.sort(key = Album_title)
print('Collection printed after using collection_sort()\n')
collection_sort(MUSIC, Album_num_tracks)
print(Collection_str(MUSIC))

#
# E-3
#
print('\n--------------E-3--------------\n ')

def unplayed_songs(MC: [Album]) -> [Songdisplay]:
    '''takes a list of Ablums and returns a list of Songdisplays,
       one for each song that has never been played
    '''
    result = []
    for a in MC:
        for s in a.songs:
            if s.play_count == 0:
                result.append(Songdisplay(a.artist, a.title, a.year, s.track, s.title, s.length, s.play_count))
    return result
assert unplayed_songs([album1]) == []
assert unplayed_songs(MUSIC) == [Songdisplay('The Rolling Stones', 'Let It Bleed', 1969, 3, 'Country Honk', 187, 0),
                                 Songdisplay('The Rolling Stones', 'Let It Bleed', 1969, 7, "You Got the Silver", 170, 0)]
for sd in unplayed_songs(MUSIC):
    print(Songdisplay_str(sd))

#
# E-4
#

def length_from_songdisplay(sd: Songdisplay) -> int:
    '''takes a Songdisplay and returns the length of the song'''
    return sd.length
assert length_from_songdisplay(songdisplay1) == 251

#
# E-5
#

def Song_listening_time(s: Song) -> int:
    '''returns the listening time of the Song'''
    return s.length * s.play_count

def Album_listening_time(A: Album) -> int:
    '''returns the listening time of all the songs in the Album'''
    total = 0
    for s in A.songs:
        total += Song_listening_time(s)
    return total

def favorite_album(MC: [Album]) -> Album:
    '''takes a list of Ablum and returns the album that is favorite'''
    collection_sort(MC, Album_listening_time)
    return MC[-1]

print('\n--------------E-5--------------\n ')
print(Album_str(favorite_album(MUSIC)))

#
# E-6
#
collection_sort(MUSIC, Album_id) # Just to put it back in the original order

def top_n(MC: [Album], n: int, keyfunction: 'Function on Albums', b: bool)->[Song]:
    '''returns a list of Songs based on the parameters'''
    list_of_Songdisplays = all_Songdisplays(MC)
    list_of_Songdisplays.sort(key=keyfunction, reverse = b)
    return list_of_Songdisplays[:n]
test_list = top_n(MUSIC, 3, play_count_from_songdisplay, True)
assert(test_list[0].s_title == "Alive and Kicking")
assert(test_list[0].a_title == "Once Upon a Time")
assert(test_list[-1].s_title == "Oh Jungleland")
assert(test_list[-1].a_title == "Once Upon a Time")

#
# E-7
#

def favorite_album2(MC: [Album], keyfunction) -> Album:
    '''takes a list of albums and returns the favorite album based on the key provided'''
    collection_sort(MC, keyfunction)
    return MC[-1]

def Song_playcount(s: Song) -> int:
    '''returns the play count of the Song'''
    return s.play_count

def Album_playcount(A: Album) -> int:
    '''returns the total playcount of all the songs in the album'''
    total = 0
    for s in A.songs:
        total += Song_playcount(s)
    return total

print('\n--------------E-7--------------\n ')
print(Album_str(favorite_album2(MUSIC, Album_listening_time)))
print(Album_str(favorite_album2(MUSIC, Album_playcount)))

#
# E-8
#

def collection_search(C: [Album], search_string: str) -> [Songdisplay]:
    '''Return a list of Songdisplays that include the input string in the album title, artist, or song title'''
    SDL = all_Songdisplays(C)
    result = []
    for sd in SDL:
        if (search_string.lower() in sd.a_title.lower() or
            search_string.lower() in sd.artist.lower() or
            search_string.lower() in sd.s_title.lower()):
            result.append(sd)
    return result

print('\n--------------E-8--------------\n ')
print(collection_search(MUSIC, 'Give'))
