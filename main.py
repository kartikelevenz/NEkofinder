#!/usr/bin/env python3
"""
UserFinder - Ethical OSINT username checker
Checks if a username exists on public platforms.
Only uses public endpoints. Respect robots.txt!
"""

import json
import argparse
import time
import sys
from urllib.parse import urljoin
import requests
from rich.console import Console
from rich.table import Table

# Suppress SSL warnings (optional)
requests.packages.urllib3.disable_warnings()

console = Console()

def load_sites():
    """Load sites from sites.json"""
    try:
        with open("sites.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        console.print("[red]❌ Error: sites.json not found![/red]")
        sys.exit(1)

def check_site(site_name, url_template, username, timeout=5):
    """Check if username exists on a site"""
    url = url_template.replace("{}", username)
    try:
        headers = {
            "User-Agent": "UserFinder (Educational OSINT Tool)"
        }
        response = requests.get(
            url,
            headers=headers,
            timeout=timeout,
            verify=False  # Skip SSL for speed (optional)
        )
        # Most sites return 200 if profile exists, 404 if not
        return response.status_code == 200
    except Exception:
        return False

def main():
    parser = argparse.ArgumentParser(description="Check username across platforms")
    parser.add_argument("username", help="Username to search for")
    parser.add_argument("--timeout", type=int, default=5, help="Request timeout (seconds)")
    args = parser.parse_args()

    console.print(f"\n[bold blue]🔍 Checking username '[cyan]{args.username}[/cyan]'...[/bold blue]\n")

    sites = load_sites()
    found = []
    not_found = []

    # Add small delay to be respectful
    for site, url_template in sites.items():
        time.sleep(0.2)  # Be kind to servers
        exists = check_site(site, url_template, args.username, args.timeout)
        if exists:
            found.append((site, url_template.replace("{}", args.username)))
            console.print(f"✅ [green]{site}[/green]: {url_template.replace('{}', args.username)}")
        else:
            not_found.append(site)
            console.print(f"❌ [red]{site}[/red]: Not found")

    # Summary
    console.print(f"\n[bold]✅ Found on {len(found)} platforms[/bold]")
    if found:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Platform", style="dim", width=15)
        table.add_column("URL")
        for site, url in found:
            table.add_row(site, url)
        console.print(table)

    console.print("\n[italic yellow]💡 Remember: Only use this for authorized OSINT![/italic yellow]")

if __name__ == "__main__":
    main()
