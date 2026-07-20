import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = "Sneaker Hunter"

TARGETS = [
    {
        "name": "Adidas UltraBoost ATR Mid Oreo",
        "model": "CG3003",
        "sizes": [
            "10.5",
            "11"
        ],
        "max_price": 150,
        "condition": "new"
    }
]


EMAIL_ENABLED = True

EMAIL_FROM = os.getenv(
    "EMAIL_FROM",
    ""
)

EMAIL_TO = os.getenv(
    "EMAIL_TO",
    ""
)
