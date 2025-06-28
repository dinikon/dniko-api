from pydantic_settings import (
    SettingsConfigDict,
    BaseSettings,
    PydanticBaseSettingsSource,
)
from config.deploy import DeploymentConfig
from config.packaging import PackagingInfo


class DNikoConfig(
    # Packaging info
    PackagingInfo,
    # Deployment configs
    DeploymentConfig,
):
    model_config = SettingsConfigDict(
        # read from dotenv format config file
        env_file=".env",
        env_file_encoding="utf-8",
        # ignore extra attributes
        extra="ignore",
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            # RemoteSettingsSourceFactory(settings_cls),
            dotenv_settings,
            file_secret_settings,
        )
