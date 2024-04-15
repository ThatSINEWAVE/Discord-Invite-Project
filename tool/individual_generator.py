import os
import json
import string
import random

MAX_FILE_SIZE_GB = 10
MAX_ROWS_PER_FILE = 1000000  # Adjust this number as needed


def generate_id(num_ids):
    base_id = 'aaaaaaaa'
    id_list = []

    for i in range(num_ids):
        current_id = base_id[:-len(str(i))] + str(i)
        id_list.append(f"ID_{i}: https://discord.gg/{current_id}")

    return id_list


def generate_discord_id():
    char_set = string.ascii_letters
    return ''.join(random.choice(char_set) for _ in range(8))


def save_to_json(id_list):
    file_num = 1
    while os.path.exists(f'../data/discord_ids_{file_num}.json'):
        file_num += 1

    file_path = f'../data/discord_ids_{file_num}.json'
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.extend(id_list)

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    num_ids = int(input("Enter the number of IDs to generate: "))
    try:
        with open('../data/discord_ids_1.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    total_generated_ids = len(data)
    total_possible_ids = 26 ** 8 * 2 ** 8  # Total possible combinations of 8-character mixed case IDs

    if total_generated_ids >= total_possible_ids:
        print("All possible IDs have been generated.")
        return

    id_list = []

    for i in range(num_ids):
        next_id = generate_discord_id()
        id_list.append(f"ID_{total_generated_ids + i}: https://discord.gg/{next_id}")

        if len(id_list) >= MAX_ROWS_PER_FILE:
            save_to_json(id_list)
            id_list = []

    save_to_json(id_list)


if __name__ == "__main__":
    main()
