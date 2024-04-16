import requests
import json


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
        return f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_hash}?size=1024"
    else:
        return "None"


def construct_banner_url(entity_id, banner_hash):
    if entity_id and banner_hash:
        return f"https://cdn.discordapp.com/banners/{entity_id}/{banner_hash}?size=1024"
    else:
        return "None"


def construct_icon_url(guild_id, icon_hash):
    if guild_id and icon_hash:
        return f"https://cdn.discordapp.com/icons/{guild_id}/{icon_hash}?size=1024"
    else:
        return "None"


def construct_splash_url(guild_id, splash_hash):
    if guild_id and splash_hash:
        return f"https://cdn.discordapp.com/splashes/{guild_id}/{splash_hash}?size=1024"
    else:
        return "None"


def main():
    invite_code = input("Enter Discord invite code: ")
    invite_details = fetch_invite(invite_code)

    if invite_details:
        convert_null_to_none(invite_details)

        # Format image URLs
        inviter_id = invite_details["inviter"]["id"]
        invite_details["inviter"]["avatar"] = construct_avatar_url(inviter_id, invite_details["inviter"].get("avatar"))
        invite_details["inviter"]["banner"] = construct_banner_url(inviter_id, invite_details["inviter"].get("banner"))

        guild_id = invite_details["guild"]["id"]  # Move this line up
        invite_details["guild"]["icon"] = construct_icon_url(guild_id, invite_details["guild"].get("icon"))
        invite_details["guild"]["banner"] = construct_banner_url(guild_id, invite_details["guild"].get("banner"))
        invite_details["guild"]["splash"] = construct_splash_url(guild_id, invite_details["guild"].get("splash"))  # Now it's safe to use guild_id

        with open("../data/discord_server_details.json", "w") as json_file:
            json.dump(invite_details, json_file, indent=4)

        print("Invite details saved to discord_server_details.json inside the data folder")


if __name__ == "__main__":
    main()
