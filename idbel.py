import httpx
from reddevil.core import get_secret, register_app

# setup reddevil
register_app(None, "settings", "")

# get odoo_secrets
odoo_secrets = get_secret("odoo")
url = odoo_secrets.get("url")
db = odoo_secrets.get("db")
username = odoo_secrets.get("username")
password = odoo_secrets.get("password")


# 2. Search and Read Partners
payload = {
    "fields": [
        "id",
        "name",
        "email",
        "x_studio_contact_nationalid_int",
        "x_studio_contact_clubid",
        "x_studio_contact_clubid_link",
    ],
    "domain": [["email", "=", "ruben.decrop@gmail.com"]],
}
headers = {
    "X-Odoo-Database": db,
    "Authorization": f"Bearer {password}",
    "Content-Type": "application/json",
}
try:
    response = httpx.post(
        url=f"{url}/json/2/res.partner/search_read",
        json=payload,
        headers=headers,
        timeout=5.0,  # 5-second timeout (default is 5.0)
    )
    results = response.json()
except Exception as e:
    raise e
print("results", results)
