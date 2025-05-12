TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'localhost',
                'port': '3306',
                'user': 'root',
                'password': '1234',
                'database': 'rio',
            }
        },
    },
    'apps': {
                "models": {
                    "models": [
                        "aerich.models",
                        "app.models.bilheteUnico",
                        "app.models.documents",
                        "app.models.typeOfDocument",
                        "app.models.user"
                        ],
                    "default_connection": "default",
            }
    }
}
