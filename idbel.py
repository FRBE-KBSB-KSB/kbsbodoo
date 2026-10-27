import httpx
from reddevil.core import get_secret, get_setting, register_app

# setup reddevil
register_app(None, "settings", "")

# odoo variables
odoo_secrets = get_secret("odoo")
odoo_params = get_setting("ODOO_CONNECTION_PARAMETERS")
url = odoo_params.get("url")
db = odoo_params.get("db")
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
print("idbel:", results[0]["x_studio_contact_nationalid_int"])
