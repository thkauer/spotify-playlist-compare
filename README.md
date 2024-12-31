 

# Spotify playlist compare
Script and utils to retrieve spotify playlist information and included tracks to
enable the comparison of playlists.

Currently the `main` script compares the tracks saved by the user with the
tracks in the playlist the user has saved, filtered by playlist author.  
The result is a set of tracks that are contained in a playlist saved by the user,
but are not contained in the tracks saved by the user.

## Configuration
To interact with the spotify api, you need to specify your api credentials.
You have the option to export the environment variables or save them in a `.env` file. 

## Usage
```
usage: main.py [-h] playlist_author

positional arguments:
  playlist_author

options:
  -h, --help       show this help message and exit
```

# Motivation
If you ask yourself **"Why is this particular use case useful for somebody?"**
or **"Why could this be possibly useful for other people?"** you have reached the right 
chapter.

And the answer:  
**Like many people, I only want to listen to the music I enjoy... right in this**
**moment, and the situation or mood im in.**  
So naturally the amount of personal playlists has grown and grown over time.
Resulting in playlists that differ completely, partially overlap or are nearly a 
complete subset of other playlists.
But the thing with taste... it can change over time.   
One day I realized that I have to sort out a chunk of songs I do not want to
listen to anymore, in general, in the type of situation or the mood the playlists are 
made for.  
Luckily spotify also added **most of the time** songs to my "Liked Songs" while adding 
them to the playlists they belong. So I started updating my playlists by iterating
trough my liked songs and updating in which playlist they should occur.  
But as highlighted in the sentence before, the songs were not always added to the "Liked 
Songs" playlist and from time to time an old song I do not like anymore and should have
been filtered out would pop up.

And now we found the reason for the current script. To not iterate trough each 
playlist (with duplicated songs between playlists) manually, checking if each song is in
the "Liked Songs" playlist.  

And finally I can listen to the music I in enjoy in the current moment without the need
to skip every second song again.  
... At least for one day after resorting all my songs.