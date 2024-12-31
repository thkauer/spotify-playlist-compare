import argparse
import sys

import spotipy
from tabulate import tabulate

from src.playlist_compare import (
    create_user_session,
    get_current_user_liked_songs,
    get_current_user_playlist_info,
    get_playlist_tracks,
)
from src.spotify_types import Playlist, Track


def main():
    # argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist_author")
    args: argparse.Namespace = parser.parse_args()
    owner_filter: str | None = args.playlist_author

    # login
    sp_session: spotipy.Spotify = create_user_session()
    print("Authenticated")

    # get current user playlist and their tracks
    print("Retrieving playlist information...")
    playlists_items: list[Playlist] = get_current_user_playlist_info(
        sp_session, owner_filter
    )
    print(f"Found {len(playlists_items)} values.")

    # output the gathered data
    print("The following playlists are found:")
    columns: list[str] = ["name", "track_count"]
    if owner_filter is None:
        columns.insert(
            1, "owner"
        )  # insert is needed to preserve the order of the Track schema
    print(
        tabulate(
            [item.model_dump(include=columns).values() for item in playlists_items],  # type: ignore
            headers=columns,
        )
    )

    # collect all track ids
    unique_playlists_track_ids: set[Track] = set()
    for playlist in playlists_items:
        unique_playlists_track_ids.update(get_playlist_tracks(sp_session, playlist.id))
    print(f"Found {len(unique_playlists_track_ids)} tracks in the queried playlists.")
    # get all saved tracks of the current user
    current_user_saved_tracks: list[Track] = get_current_user_liked_songs(sp_session)
    if current_user_saved_tracks is None:
        print("No tracks for the current user are found! Quitting...")
        sys.exit()
    print(f"Found {len(current_user_saved_tracks)} liked songs.")
    # compare track ids to the current user´s saved tracks
    print(
        "Searching for song differences between playlist saved songs"
        + "and the liked songs."
    )
    unique_liked_songs: set[Track] = set(current_user_saved_tracks)
    song_difference: set[Track] = unique_playlists_track_ids.difference(
        unique_liked_songs
    )
    print(f"Found {len(song_difference)} differences:")
    print(tabulate([song.model_dump() for song in song_difference]))


if __name__ == "__main__":
    main()
