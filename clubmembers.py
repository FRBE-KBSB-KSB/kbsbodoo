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


user_profile = models.execute_kw(
    db, uid, password, "res.users", "read", [[uid]], {"fields": profile_fields}
)

print("\n--- Basic User Profile ---")
print(user_profile[0])

# -------------------------------------------------------------
# OPTIONAL STEP 3: Fetch linked Contact/Partner profile details
# -------------------------------------------------------------
# Odoo links users to a res.partner record for extended profile data (phone, address, avatar, etc.)
partner_id = user_profile[0]["partner_id"][0]

partner_fields = [
    "name",
    "email",
    "x_studio_contact_nationalid_int",
]

partner_profile = models.execute_kw(
    db, uid, password, "res.partner", "read", [[partner_id]], {"fields": partner_fields}
)

print("\n--- Full Contact Profile ---")
print(partner_profile[0])
