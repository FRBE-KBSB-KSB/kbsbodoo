import xmlrpc.client

url = "https://frbe-kbsb.odoo.com"
db = "frbe-kbsb"
username = "ruben.decrop@frbe-kbsb-ksb.be"
password = "7c92492a86877cca7b10ae31b1476153b0815380"

# 1. Connect to Common Endpoint for Authentication
common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

# Fetch model metadata using fields_get
# You can optionally pass attributes to limit returned metadata fields
fields_info = models.execute_kw(
    db,
    uid,
    password,
    "res.partner",
    "fields_get",
    [],
    {"attributes": ["string", "type", "required"]},
)

# Print field names and their types
for field_name, meta in fields_info.items():
    print(f"{field_name}: {meta.get('string')} ({meta.get('type')})")
