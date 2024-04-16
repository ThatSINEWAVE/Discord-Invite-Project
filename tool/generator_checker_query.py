import requests
import re
import json
import string
import random


def extract_invite_code(link):
    match = re.search(r'(?:discord\.gg/|discord\.com/invite/)([a-zA-Z0-9]+)', link)
    if match:
        return match.group(1)
    else:
        return None


def is_invite_active(invite):
    invite_code = extract_invite_code(invite)
    if not invite_code:
        print("Invalid invite link format.")
        return False
    api_url = f"https://discord.com/api/v9/invites/{invite_code}?with_counts=true&with_expiration=true"
    response = requests.get(api_url)
    if response.status_code == 404:
        return False  # Invite not found
    try:
        data = response.json()
        if 'message' in data and data['message'] == 'Unknown Invite':
            return False  # Invite is unknown
        else:
            return True  # Invite is active
    except ValueError:
        return False  # Error parsing JSON


def fetch_invite(invite_code):
    if not invite_code:
        return None

    url = f'https://discord.com/api/v8/invites/{invite_code}?with_counts=true'
    response = requests.get(url)

    if response.ok:
        return response.json()
    else:
        print("Failed to fetch invite details.")
        return None


def convert_null_to_none(obj):
    for key, value in obj.items():
        if value is None:
            obj[key] = "None"
        elif isinstance(value, dict):
            convert_null_to_none(value)


def construct_avatar_url(user_id, avatar_hash):
    if user_id and avatar_hash:
        return f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}.webp?size=1024"
    else:
        return "None"


def construct_banner_url(entity_id, banner_hash):
    if entity_id and banner_hash:
        return f"https://cdn.discordapp.com/banners/{entity_id}/{banner_hash}.webp?size=1024"
    else:
        return "None"


def construct_icon_url(guild_id, icon_hash):
    if guild_id and icon_hash:
        return f"https://cdn.discordapp.com/icons/{guild_id}/{icon_hash}.webp?size=1024"
    else:
        return "None"


def generate_invite_link():
    characters = string.ascii_letters + string.digits
    invite_code = ''.join(random.choice(characters) for _ in range(7))
    return f"https://discord.gg/{invite_code}"


def main():
    num_invites = int(input("Enter the number of invite links to generate, check, and query: "))

    invite_details = []

    for _ in range(num_invites):
        invite_link = generate_invite_link()
        invite_code = extract_invite_code(invite_link)

        if is_invite_active(invite_link):
            invite_data = fetch_invite(invite_code)

            if invite_data:
                convert_null_to_none(invite_data)

                # Format image URLs
                inviter_id = invite_data["inviter"]["id"]
                invite_data["inviter"]["avatar"] = construct_avatar_url(inviter_id, invite_data["inviter"].get("avatar"))
                invite_data["inviter"]["banner"] = construct_banner_url(inviter_id, invite_data["inviter"].get("banner"))

                guild_id = invite_data["guild"]["id"]
                invite_data["guild"]["icon"] = construct_icon_url(guild_id, invite_data["guild"].get("icon"))
                invite_data["guild"]["banner"] = construct_banner_url(guild_id, invite_data["guild"].get("banner"))

                invite_details.append(invite_data)
        else:
            expired_invite_details = {
                "type": "expired",
                "code": invite_code,
                "inviter": "expired",
                "expires_at": "expired",
                "flags": "expired",
                "guild": "expired",
                "guild_id": "expired",
                "channel": "expired",
                "approximate_member_count": "expired",
                "approximate_presence_count": "expired"
            }
            invite_details.append(expired_invite_details)

    with open("../data/discord_server_details.json", "w") as json_file:
        json.dump(invite_details, json_file, indent=4)

    print("Invite details saved to discord_server_details.json")


if __name__ == "__main__":
    main()
