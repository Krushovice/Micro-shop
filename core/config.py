from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str
    ECHO: True

    @property
    def db_url(self):
        return f"{self.DB_URL}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
