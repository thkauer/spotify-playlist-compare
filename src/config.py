from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    spotipy_client_id: str
    spotipy_client_secret: str
    spotipy_redirect_url: str = "http://localhost"


SETTINGS = _Settings(_env_file=".env")  # type:ignore

if __name__ == "__main__":
    print(SETTINGS)
