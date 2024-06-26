<div align="center">

# [The Discord Invite Project](https://thatsinewave.github.io/Discord-Invite-Project)

Welcome to The Discord Invite Project! This repository serves as an educational and research platform exploring the concept of creating a database to track and analyze Discord invite links. 
The project aims to assist in Open Source Intelligence (OSINT) investigations by providing tools to identify and study Discord servers, including potentially malicious ones.

</div>

## About the Project

The Discord Invite Project revolves around the idea of building a comprehensive database of Discord invite links for research purposes. 
By checking the Discord API, this database could potentially reveal valuable information about the creators of invites, server creators, and other metadata associated with Discord servers.

<div align="center">

# [Join my discord server](https://discord.gg/2nHHHBWNDw)

</div>

### Concept Status

As of now, The Discord Invite Project is in a conceptual phase. 
The primary challenge lies in the immense scale of data that would need to be stored and processed. 
The database's size is estimated to be almost **7 terabytes** with exactly **208,827,064,576 rows** of data just for the index file storing all the invite links. The estimated amount for the full database containing details about EVERY invite link would come up to around **170 terabytes** requiring substantial processing power to effectively manage, analyze or just query.
The plan is to turn this tool into a powerful search engine dedicated to researching discord users and servers associated with malicious and illegal activities.

### Capabilities

- Check for which servers a particular user has created invites using the user's Discord ID.
- Check correlations between users and servers using the user's Discord ID or a server's Guild ID.
- Check for all active invites created for a specific server using the server's Guild ID.
- Verify what users have created invites for a certain server and when using the user's Discord ID.
- Chart common emojis and ToS emojis across servers using emoji IDs.
- Full history charts and graphs to visualise data and establish correlations easier.
- Many more data analysis methods coming soon.

**NOTE**: All capabilities covered by this tool are possible using **PUBLIC INFORMATION** freely available for anyone.


<div align="center">

## ☕ [Support my work on Ko-Fi](https://ko-fi.com/thatsinewave)

</div>

## Repository Contents

- `data/active_invites.json`: Example file containing active generated invite links.
- `data/inactive_invites.json`: Example file containing inactive generated invite links.
- `data/discord_invites_1.json`: Example file containing a list of 10 Discord invite links.
- `data/discord_server_details.json`: Example file of a successful API query.
- `tools/individual_checker.py`: Script to check the validity and activity status of individual Discord invite links.
- `tools/individual_generator.py`: Script to generate Discord invite links and save them to JSON files.
- `tools/individual_query.py`; Script to query the API for full details about a specific invite link and save it to a JSON file.
- `tools/generator_checker.py`: Script combining generation and checking functionalities for Discord invite links.
- `tools/generator_checker_query.py`: Script combining all individual scripts into one powerful invite link generator, checker and API query tool.
- `images/`: GitHub Pages. (Please ignore)
- `index.html`: GitHub Pages. (Please ignore)
- `about.html`: GitHub Pages. (Please ignore)
- `styles.css`: GitHub Pages. (Please ignore)
- `script.js` GitHub Pages. (Please ignore)

## Contributing

Contributions to The Discord Invite Project are welcome! Whether it's through code contributions, suggestions, or collaborations in hosting and developing the project further, your input is valued. 
Together, we can work towards making this project a valuable tool for researchers the future.

### Get Involved

If you're interested in contributing or collaborating on The Discord Invite Project, feel free to reach out and get involved! 
Let's work together to turn this concept into a valuable resource for the research community.

### License

This project is open-source and available under the GLWTS Public License. See the LICENSE file for more details.

## Disclaimer

It's important to note that utilizing the scripts provided in this repository, particularly the `individual_checker.py` and `generator_and_checker.py`, may lead to IP bans from Discord servers or even account suspensions. 
The author takes no responsibility for any consequences resulting from the misuse of these scripts. 
This repository is intended solely for educational and research purposes.
