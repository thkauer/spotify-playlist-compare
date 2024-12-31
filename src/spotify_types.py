from __future__ import annotations

from pydantic import BaseModel


class Playlist(BaseModel):
    id: str
    name: str
    owner: str
    track_count: int
    tracks: list[Track] | None = None


class Track(BaseModel):
    id: str
    name: str
    artists: list[str]

    def __eq__(self, value: object) -> bool:
        match value:
            case Track():
                if self.id == value.id:
                    return True
            case str():
                if self.id == value:
                    return True
        return False

    def __hash__(self) -> int:
        return hash(self.id)
