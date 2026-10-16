import asyncio
import re

import httpx

ODOO_URL = "https://frbe-kbsb.odoo.com"
DB = "frbe-kbsb"
USER = "ruben.decrop@gmail.com"



async def main():
    async with httpx.AsyncClient(base_url=ODOO_URL, follow_redirects=True) as client:
        # 1. Loginpagina ophalen voor CSRF
        response = await client.get("/web/login")
        csrf_match = re.search(r'name="csrf_token" value="([^"]+)"', response.text)
        if not csrf_match:
            raise RuntimeError("Could not find CSRF token on the login page")

        # 2. Login en wachtwoord versturen
        response = await client.post(
            "/web/login",
            data={
                "login": USER,
                "password": PASSWORD,
                "csrf_token": csrf_match.group(1),
                "db": DB,
            },
        )

        # 3. Vraag de code op als 2FA actief is
        if "/web/login/totp" in str(response.url):
            print("2FA is actief voor deze gebruiker")
            csrf_match = re.search(r'name="csrf_token" value="([^"]+)"', response.text)
            if not csrf_match:
                raise RuntimeError("Could not find CSRF token on the 2FA page")

            totp_token = await asyncio.to_thread(input, "TOTP-code: ")
            response = await client.post(
                "/web/login/totp",
                data={
                    "totp_token": totp_token.strip(),
                    "csrf_token": csrf_match.group(1),
                },
            )

        print(f"Login response: {response.url}")


if __name__ == "__main__":
    asyncio.run(main())
