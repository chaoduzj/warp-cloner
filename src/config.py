from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

class 设置(BaseSettings):
    model_config =  SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    BASE_KEYS: list[str] = Field(
        validation_alias='BASE_KEYS',
        default=[
            'CQr753G0-L7Jm6j51-3N1Uw7j9',
            '6hFkP924-56Ys1Gm9-84xF1QP3',
            'bZ3iI986-XsD3F960-xn9ie201',
            '08Otin43-6U52C0fD-0Td26hi5',
            'F79fE1U3-Y9K074kj-R320xW6u',
            '90H8x7ZN-GNq754r2-25r9wn1Q',
            'T5C9l87B-q7af86n1-62S0R5kq',
            'M61V30UC-W4Q03nR7-Y5T2nb74',
            '71B4JF5r-vEmY6570-47w85QcJ',
            'm5x67hV4-3W4t7FJ8-2O4ZJ6r7',
        ]
    )
    THREADS_COUNT: int = Field(validation_alias='THREADS_COUNT', default=1)
    PROXY_FILE: str | None = Field(validation_alias='PROXY_FILE', default=None)
    DEVICE_MODELS: list[str] = Field(validation_alias='DEVICE_MODELS', default=[])
    WEBHOOK_KEY_URL: str | None = Field(validation_alias='WEBHOOK_KEY_URL', default=None)
    SAVE_WIREGUARD_VARIABLES: bool = Field(validation_alias='SAVE_WIREGUARD_VARIABLES', default=False)
    DELAY: int = Field(validation_alias='DELAY', default=25)
    OUTPUT_FILE: str = Field(validation_alias='OUTPUT_FILE', default='output.txt')
    OUTPUT_FORMAT: str = Field(validation_alias='OUTPUT_FORMAT', default='{key} | {referral_count}')
    RETRY_COUNT: int = Field(validation_alias='RETRY_COUNT', default=3)


config = Settings()

