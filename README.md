# Spotify playlist compare
Script and utils to retrieve Spotify playlist information and included tracks to
enable playlist comparison.

Currently the `main` script compares the tracks saved by the user with the
tracks in the playlist saved by the user, filtered by the playlist author.  
The result is a set of tracks that are in a user-saved playlist but not in the 
user-saved tracks.

## Configuration
In order to interact with the Spotify API, you will need to provide your API credentials.
You have the option to export the environment variables or save them to an `.env` file. 

## Usage
```
usage: main.py [-h] playlist_author

positional arguments:
  playlist_author

options:
  -h, --help       show this help message and exit
```

# Motivation
If you ask yourself, **"Why is this particular use case useful to someone?"**
or **"Why could this be possibly be useful for other people?"**, you have come to the 
right chapter.

And the answer:  
**Like many people, I only want to listen to the music I like... right in the**
**moment, and in the situation or mood I am in.**  
So naturally, the number of personal playlists has grown and grown over time.
Resulting in playlists that are completely different, partially overlapping or almost a 
complete subset of other playlists.
But the thing about taste... it can and will change over time.   
One day I realized that I needed to sort out a bunch of songs that I no longer wanted to
listen to in the kind of situation or mood the playlists were made for.  
Luckily Spotify also added **most of the time** songs to my "Liked Songs" while adding 
them to the playlists they belong to. So I started updating my playlists by iterating
through my Liked Songs and updating which playlist they should appear in.  
But as the previous sentence indicates, the songs were not always added to the "Liked 
Songs" playlist, and from time to time an old song that I no longer like and should have
been filtered out would pop up.

And now we have found the reason for the current script. To not have to manually iterate through each playlist (with duplicate songs between playlists) to check if each song is
in the "Liked Songs" playlist.  

And finally I can listen to the music I like without having to skip every second song.  
... At least for a day after resorting all of my songs.