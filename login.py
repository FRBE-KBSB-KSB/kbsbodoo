import asyncio

import httpx

ODOO_URL = "https://frbe-kbsb.odoo.com"
DB = "frbe-kbsb"
USER = "ruben.decrop@gmail.com"



async def main():
    async with httpx.AsyncClient(base_url=ODOO_URL) as client:
        # Authenticate
        auth_resp = await client.post(
            "/web/session/authenticate",
            json={
                "jsonrpc": "2.0",
                "params": {"db": DB, "login": USER, "password": PASSWORD},
                "id": 1,
            },
        )
        data = auth_resp.json().get("result")
        if not data or not data.get("uid"):
            print("Login failed", auth_resp.status_code, auth_resp.json())
            return

        print(f"Async authenticated for User ID: {data['uid']}")

        # Call endpoint
        read_resp = await client.post(
            "/web/dataset/call_kw",
            json={
                "jsonrpc": "2.0",
                "method": "call",
                "params": {
                    "model": "res.partner",
                    "method": "search_read",
                    "args": [[]],
                    "kwargs": {"fields": ["name"], "limit": 3},
                },
                "id": 2,
            },
        )
        print(read_resp.json().get("result"))


asyncio.run(main())
