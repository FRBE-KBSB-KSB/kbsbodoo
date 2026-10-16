import xmlrpc.client

url = "https://frbe-kbsb.odoo.com"
db = "frbe-kbsb"
username = "ruben.decrop@gmail.com"  # Portal user login
password = "wz1knbgGM"  # Password or API Key

# 1. Authenticate to get User ID (uid)
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})

if not uid:
    raise Exception(
        "Authentication failed: Check DB name, username, or password/API key."
    )

print(f"Successfully authenticated! User ID (uid): {uid}")


models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# Read key profile fields from res.users
profile_fields = [
    "partner_id",
]

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
