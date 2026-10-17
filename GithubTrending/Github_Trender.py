
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ╔══════════════════════════════════════════════════════════════╗
# ║                     🚀 GITHUB TRENDER                        ║
# ╠══════════════════════════════════════════════════════════════╣
# ║  Project     : GitHub Trender                                ║
# ║  Author      : SwiftGlitxh                                   ║
# ║  Version     : 1.1.0                                         ║
# ║  Description : Discover popular new GitHub repositories.     ║
# ╠══════════════════════════════════════════════════════════════╣
# ║  Usage       : python trender.py                             ║
# ║  Requires    : requests, rich                                ║
# ╚══════════════════════════════════════════════════════════════╝

from datetime import datetime, timedelta, timezone

import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

console = Console()

API_URL = "https://api.github.com/search/repositories"


def main():
    console.print()

    console.print(
        Panel.fit(
            "[bold cyan]🚀 GITHUB TRENDER[/bold cyan]\n"
            "[dim]Discover the hottest new repositories[/dim]\n\n"
            "[green]👨‍💻 Developer:[/green] SwiftGlitxh\n"
            "[yellow]📦 Version:[/yellow] 1.1.0",
            border_style="bright_blue",
            padding=(1, 4),
        )
    )

    console.print()

    language = Prompt.ask(
        "[bold cyan]💻 Programming language[/bold cyan] "
        "[dim](Enter for all)[/dim]",
        default="",
        show_default=False,
    ).strip()

    week_ago = (
        datetime.now(timezone.utc) - timedelta(days=7)
    ).strftime("%Y-%m-%d")

    search = f"created:>{week_ago}"

    if language:
        search += f" language:{language}"

    console.print()
    console.print(
        f"🔎 [cyan]Language:[/cyan] "
        f"[bold]{language or 'All Languages'}[/bold]"
    )
    console.print(
        "📅 [cyan]Period:[/cyan] Last 7 days"
    )
    console.print(
        "⭐ [cyan]Sort by:[/cyan] Most stars"
    )
    console.print()

    try:
        with console.status(
            "[bold cyan]🌐 Searching GitHub repositories...[/bold cyan]",
            spinner="dots",
        ):
            response = requests.get(
                API_URL,
                params={
                    "q": search,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 10,
                },
                headers={
                    "Accept": "application/vnd.github+json",
                    "User-Agent": "GitHub-Trender",
                },
                timeout=15,
            )

            response.raise_for_status()
            data = response.json()

    except requests.exceptions.Timeout:
        console.print(
            "[bold red]❌ Request timed out. Try again.[/bold red]"
        )
        return

    except requests.exceptions.HTTPError:
        console.print(
            f"[bold red]❌ GitHub API error: "
            f"{response.status_code}[/bold red]"
        )

        if response.status_code == 403:
            console.print(
                "[yellow]⚠️ API rate limit may have been reached.[/yellow]"
            )
        return

    except requests.exceptions.RequestException as error:
        console.print(f"[bold red]❌ Network error: {error}[/bold red]")
        return

    repos = data.get("items", [])

    if not repos:
        console.print(
            Panel(
                "😕 No repositories found.\n"
                "Try another programming language.",
                title="No Results",
                border_style="yellow",
            )
        )
        return

    table = Table(
        title="🔥 TOP 10 TRENDING GITHUB REPOSITORIES",
        title_style="bold bright_cyan",
        header_style="bold magenta",
        border_style="bright_blue",
        show_lines=True,
        expand=True,
    )

    table.add_column("🏆 #", justify="center", style="cyan", width=5)
    table.add_column("📦 Repository", style="bold white")
    table.add_column("⭐ Stars", justify="right", style="yellow")
    table.add_column("🔗 GitHub URL", style="bright_blue")

    for number, repo in enumerate(repos, start=1):
        name = repo["full_name"]
        stars = repo["stargazers_count"]
        url = repo["html_url"]

        if number == 1:
            rank = "🥇"
        elif number == 2:
            rank = "🥈"
        elif number == 3:
            rank = "🥉"
        else:
            rank = str(number)

        table.add_row(
            rank,
            name,
            f"{stars:,}",
            f"[link={url}]{url}[/link]",
        )

    console.print(table)
    console.print()

    total = data.get("total_count", 0)

    console.print(
        Panel(
            f"📊 [green]Repositories found:[/green] "
            f"[bold]{total:,}[/bold]\n"
            f"🏆 [green]Top results displayed:[/green] "
            f"[bold]{len(repos)}[/bold]\n"
            f"💻 [green]Language:[/green] "
            f"[bold]{language or 'All'}[/bold]",
            title="📈 Search Summary",
            border_style="green",
        )
    )

    console.print()
    console.print(
        "[dim]⚡ Powered by GitHub API | "
        "Developed by SwiftGlitxh[/dim]",
        justify="center",
    )
    console.print()


if __name__ == "__main__":
    main()
