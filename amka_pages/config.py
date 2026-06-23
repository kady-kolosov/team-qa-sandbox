import os
import time
from dotenv import load_dotenv


load_dotenv()


class AmkaConfig:
    # BASE_AUTH_USERNAME = os.getenv("BASIC_AUTH_USERNAME")
    # BASE_AUTH_PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")
    # BASE_URL = (
    #     f"https://{BASE_AUTH_USERNAME}:{BASE_AUTH_PASSWORD}@www.example.ru"
    # )
    BASE_URL = (
        f"https://www.amediateka.ru"
    )
    AMKA_AUTH_USERNAME = os.getenv("AMKA_AUTH_USERNAME")
    AMKA_AUTH_PASSWORD = os.getenv("AMKA_AUTH_PASSWORD")

    @staticmethod
    def generate_credentials(
        email: str | None = None, password: str | None = None
    ) -> tuple[str, str]:
        if email is None:
            email = f"test_{int(time.time())}@test.com"
        if password is None:
            password = f"test_%P{int(time.time())}P%"

        return email, password
