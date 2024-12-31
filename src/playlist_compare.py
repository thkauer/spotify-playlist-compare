from typing import Any

from pydantic import ValidationError
from spotipy import Spotify, SpotifyOAuth

from src.config import SETTINGS
from src.spotify_types import Playlist, Track

SCOPE = ["playlist-read-private", "user-library-read"]


def get_current_user_playlist_info(
    sp: Spotify, filter_owner: str | None = None, fetch_track_info: bool = False
) -> list[Playlist]:
    playlists_response_json: dict[str, Any] | None = sp.current_user_playlists()

    playlists_items: list[Playlist] = []
    while playlists_response_json:
        playlist: dict[str, Any]
        for playlist in playlists_response_json["items"]:
            # filter by owner if an owner is given
            playlist_owner: str | None = playlist["owner"]["display_name"]
            if filter_owner is not None and playlist_owner != filter_owner:
                continue

            playlist["owner"] = playlist_owner
            playlist["track_count"] = playlist["tracks"]["total"]

            # extract track information if requested
            if fetch_track_info:
                playlist["tracks"] = get_playlist_tracks(sp, playlist["id"])
            else:
                del playlist["tracks"]
            playlists_items.append(Playlist.model_validate(playlist))

        if playlists_response_json["next"] is None:
            break
        playlists_response_json = sp.next(playlists_response_json)

    return playlists_items


def get_playlist_tracks(sp: Spotify, playlist_id: str) -> list[Track]:
    """Get the tracks of the playlist. Local files are ignored."""
    tracks: list[Track] = []

    playlist_data: dict[str, Any] | None = sp.playlist_items(playlist_id)
    if not playlist_data:
        return []

    track_data: dict[str, Any]
    try:
        for item in playlist_data["items"]:
            track_data = item["track"]
            if track_data["is_local"]:
                continue
            track_data["artists"] = [artist["name"] for artist in track_data["artists"]]
            tracks.append(Track.model_validate(track_data))
    except ValidationError as exc:
        print(track_data)
        raise exc
    return tracks


def get_current_user_liked_songs(sp: Spotify) -> list[Track]:
    saved_tracks_response_json: dict[str, Any] | None = sp.current_user_saved_tracks()
    if not saved_tracks_response_json:
        return []

    tracks: list[Track] = []
    while saved_tracks_response_json:
        track_json: dict[str, Any]
        for track_json in [
            item["track"] for item in saved_tracks_response_json["items"]
        ]:
            track_json["artists"] = [artist["name"] for artist in track_json["artists"]]
            tracks.append(Track.model_validate(track_json))

        if not saved_tracks_response_json["next"]:
            break
        saved_tracks_response_json = sp.next(saved_tracks_response_json)

    return tracks


def create_user_session() -> Spotify:
    sp = Spotify(
        auth_manager=SpotifyOAuth(
            SETTINGS.spotipy_client_id,
            SETTINGS.spotipy_client_secret,
            SETTINGS.spotipy_redirect_url,
            scope=SCOPE,
        )
    )
    return sp
