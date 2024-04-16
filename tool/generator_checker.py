import requests
import re
import json


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


def generate_and_check_invites():
    with open("generated_invites.json", "r") as f:
        generated_invites = json.load(f)

    active_invites = []

    for invite in generated_invites:
        if is_invite_active(invite):
            active_invites.append(invite)

    with open("active_invites.json", "w") as f:
        json.dump(active_invites, f, indent=4)

    print("Active invites have been saved to active_invites.json.")


generate_and_check_invites()
