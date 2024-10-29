- Data was scraped using the GitHub API, focusing on users in Sydney with over 100 followers and their repository information.
- A surprising insight was that many repositories had no watchers despite a high follower count.
- Developers in Sydney should consider increasing repository visibility by engaging more with the community.

### Project Overview
This project collects GitHub users in Sydney with over 100 followers and their repositories, saving the data in CSV format.

### Data Collection Process
1. The script calls the GitHub API to gather user and repository information.
2. User data is saved in `users.csv`, and repository data is saved in `repositories.csv`.

### Dependencies
- Python 3
- Requests module (`pip install requests`)
