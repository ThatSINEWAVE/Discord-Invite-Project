import requests
import re


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


invite_link = input("Enter the Discord invite link: ").strip()
if is_invite_active(invite_link):
    print("Invite is active.")
else:
    print("Invite is not active.")
