from dataclasses import dataclass
import os

YOUTUBE_API_KEY = "API_KEY"

@dataclass
class EnvironmentVariable:
    Key=os.getenv(YOUTUBE_API_KEY)


env_var = EnvironmentVariable()