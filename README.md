# 🚀 GitHub Trender
<img width="2048" height="768" alt="image" src="https://github.com/user-attachments/assets/43ac684b-6079-47ee-b638-890a9f1c3a9f" />

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![GitHub API](https://img.shields.io/badge/GitHub-REST_API-181717?logo=github)
![Version](https://img.shields.io/badge/Version-1.1.0-brightgreen)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)

**GitHub Trender** is a lightweight, Python-based command-line tool that discovers the most-starred GitHub repositories created within the last 7 days.

Built with a clean, colourful terminal interface using [Rich](https://github.com/Textualize/rich), GitHub Trender makes discovering new open-source projects simple and visually appealing.

Developed by **SwiftGlitxh**.

---

## ✨ Features

- 🔥 **Discover Popular Repositories** — Find newly created GitHub repositories ranked by total stars.
- 💻 **Language Filtering** — Search Python, JavaScript, Rust, Go, C++, and more.
- 🏆 **Top 10 Rankings** — Displays the 10 most-starred matching repositories.
- 🥇 **Ranking Medals** — Gold, silver, and bronze medals for the top three results.
- 🎨 **Beautiful Terminal UI** — Coloured tables, borders, panels, and emojis powered by Rich.
- 🔗 **Clickable Repository Links** — Open repositories directly from supported terminals.
- 📊 **Search Statistics** — View matching repository counts and search details.
- ⏳ **Loading Animation** — Animated spinner while fetching results.
- 🛡️ **Error Handling** — Handles network failures, request timeouts, and GitHub API errors.
- 🔑 **No API Key Required** — Uses GitHub's public REST API.

## 🖥️ Example Output

```text
╭──────────────────────────────────────────╮
│                                          │
│           🚀 GITHUB TRENDER              │
│                                          │
│   Discover the hottest new repositories  │
│                                          │
│   👨‍💻 Developer: SwiftGlitxh               │
│   📦 Version: 1.1.0                      │
│                                          │
╰──────────────────────────────────────────╯

💻 Programming language: Python

🔎 Language: Python
📅 Period: Last 7 days
⭐ Sort by: Most stars

🔥 TOP 10 TRENDING GITHUB REPOSITORIES

Rank  Repository                  Stars
────────────────────────────────────────
🥇    example/ai-assistant         4,820
🥈    example/python-tools         3,150
🥉    example/automation           2,740
4     example/security-kit         1,920

📈 Search Summary
🏆 Top results displayed: 10
💻 Language: Python

⚡ Powered by GitHub API
   Developed by SwiftGlitxh
```

*Example data shown above is illustrative, not live GitHub data.*

## 📋 Requirements

- Python 3.9 or newer
- Internet connection
- `requests` library
- `rich` library

Compatible with Windows, Linux, and macOS.

## 📥 Installation

**1. Clone the repository**

```bash
git clone https://github.com/SwiftGlitxh/GitHub-Trender.git
```

**2. Navigate into the project directory**

```bash
cd GitHub-Trender
```

**3. Install the required dependencies**

```bash
python -m pip install requests rich
```

**4. Run GitHub Trender**

```bash
python trender.py
```

> On some Linux and macOS systems, use `python3` instead of `python`.

## 🚀 Usage

Start the application:

```bash
python trender.py
```

When prompted, enter a programming language:

```text
💻 Programming language (Enter for all): Python
```

GitHub Trender will search for newly created Python repositories and display the 10 most-starred results.

**Search all programming languages**

Simply press `Enter` without typing anything.

```text
💻 Programming language (Enter for all):
```

**Search a specific language**

```text
💻 Programming language (Enter for all): JavaScript
```

Other examples include:

- `Python`
- `JavaScript`
- `TypeScript`
- `Rust`
- `Go`
- `Java`
- `C++`
- `C#`

## ⚙️ How It Works

GitHub Trender uses the official [GitHub REST API](https://docs.github.com/en/rest/search/search#search-repositories).

**1. Calculate the date**

The script calculates the date seven days before the current UTC date.

**2. Build the search query**

For all languages:

```text
created:>2026-10-10
```

For Python repositories:

```text
created:>2026-10-10 language:Python
```

The date above is an example.

**3. Query the GitHub API**

```text
GET https://api.github.com/search/repositories
```

Using these parameters:

| Parameter | Value | Description |
|---|---|---|
| `q` | Search query | Filters by creation date and language |
| `sort` | `stars` | Sorts by total stars |
| `order` | `desc` | Highest first |
| `per_page` | `10` | Returns up to 10 repositories |

**4. Display the results**

The application formats the API response into a styled terminal table showing repository names, star counts, rankings, and GitHub URLs.

## 📁 Project Structure

```text
GitHub-Trender/
│
├── trender.py         # Main Python application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

### requirements.txt

```text
requests
rich
```

Install all dependencies with:

```bash
python -m pip install -r requirements.txt
```

## ⚠️ GitHub API Rate Limits

GitHub Trender uses GitHub's public Search API without authentication.

Unauthenticated search requests are subject to GitHub's search rate limits, typically **10 requests per minute**.

If the limit is exceeded, the application may display:

```text
❌ GitHub API error: 403
⚠️ API rate limit may have been reached.
```

Wait before trying again.

For additional information, see the [GitHub API rate limit documentation](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api).

## 📝 Important Notes

- GitHub Trender searches repositories **created recently**, rather than repositories that gained the most stars recently.
- Star counts represent total stars at the time of the search.
- Results depend on the GitHub Search API and its indexing.
- An internet connection is required.
- No GitHub account or personal access token is required.
- Some terminal applications may not support clickable links or render every emoji correctly.

## 🛠️ Built With

- [Python](https://www.python.org/) — Core programming language
- [Requests](https://requests.readthedocs.io/) — HTTP requests
- [Rich](https://github.com/Textualize/rich) — Terminal styling and formatting
- [GitHub REST API](https://docs.github.com/en/rest) — Repository search data

## 🗺️ Future Improvements

Planned features for future versions:

- [ ] Custom date ranges (7, 30, and 90 days)
- [ ] Customisable number of results
- [ ] Export results to JSON
- [ ] Export results to CSV
- [ ] Search repositories by topic
- [ ] Filter by minimum star count
- [ ] Display repository descriptions
- [ ] GitHub authentication for higher API limits
- [ ] Interactive terminal menu

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

Please keep contributions clean, readable, and consistent with the project's beginner-friendly design.

## 👨‍💻 Author

**SwiftGlitxh**

GitHub: [github.com/SwiftGlitxh](https://github.com/SwiftGlitxh)

---

**⭐ If you find GitHub Trender useful, consider starring the repository!**

*Made with Python 🐍 | Powered by GitHub API 🚀*
