from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    DB_URL: str
    ECHO: bool = True

    @property
    def db_url(self):
        return f"{self.DB_URL}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
