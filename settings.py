GOOGLE_PROJECT_ID = "website-kbsb-prod"

ODOO_CONNECTION_PARAMETERS = {
    "url": "https://frbe-kbsb.odoo.com",
    "db": "frbe-kbsb",
    "timeout": 10.0,
    "max_keepalive": 20,
    "max_connections": 100,
}

SECRETS = {
    "odoo": {
        "name": "kbsb-odoo",
        "manager": "googlejson",
    },
    "salt": {
        "name": "kbsb-salt",
        "manager": "googlejson",
    },
}
