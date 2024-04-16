import requests
import re
import json
import string
import random

def extract_invite_code(link):
    # Extract the invite code from the link using regex
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


def generate_random_invite():
    characters = string.ascii_letters + string.digits
    invite_code = ''.join(random.choice(characters) for _ in range(7))
    return f"https://discord.gg/{invite_code}"


def main():
    target_active_invites = int(input("Enter the number of active invites you want to find: "))
    print(f"Searching for {target_active_invites} active Discord invites...")

    active_invites = []
    inactive_invites = []

    while len(active_invites) < target_active_invites:
        invite_link = generate_random_invite()
        print(f"Checking invite: {invite_link}")

        if is_invite_active(invite_link):
            active_invites.append(invite_link)
            print(f"Found an active invite: {invite_link}")
        else:
            inactive_invites.append(invite_link)
            print(f"Invite is inactive: {invite_link}")

    with open("../data/active_invites.json", "w") as f:
        json.dump(active_invites, f, indent=4)

    with open("../data/inactive_invites.json", "w") as f:
        json.dump(inactive_invites, f, indent=4)

    print(f"Found {len(active_invites)} active invites.")
    print("Active invites have been saved to active_invites.json.")
    print("Inactive invites have been saved to inactive_invites.json.")


if __name__ == "__main__":
    main()