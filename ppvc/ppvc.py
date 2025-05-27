#!/usr/bin/env python3

import json
import sys
from typing import List, Union
from urllib import request
from urllib.error import HTTPError, URLError
from packaging.version import parse as parse_version
from rich.console import Console
from rich.table import Table
from rich import print as rprint


def get_package_versions(pkg_name: str, latest_only: bool = False) -> List[str]:
    """
    Fetch available versions of a Python package from PyPI.
    
    Args:
        pkg_name: Name of the package to check
        latest_only: If True, returns only the latest version
        
    Returns:
        List of version strings sorted in descending order (latest first)
        
    Raises:
        HTTPError: If the package is not found on PyPI
        URLError: If there's a network connection issue
    """
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    
    try:
        with request.urlopen(url) as response:
            releases = json.loads(response.read())['releases']
    except HTTPError as e:
        raise HTTPError(f"Package '{pkg_name}' not found on PyPI") from e
    except URLError as e:
        raise URLError(f"Network error while fetching package '{pkg_name}'") from e
    
    versions = sorted(releases, key=parse_version, reverse=True)
    return [versions[0]] if latest_only else versions


def display_versions(pkg_name: str, versions: List[str]) -> None:
    """
    Display versions in a formatted table with colors.
    
    Args:
        pkg_name: Name of the package
        versions: List of version strings
    """
    console = Console()
    
    if len(versions) == 1:
        # Single version display
        console.print(f"\n[bold green]Latest version of {pkg_name}:[/bold green]")
        console.print(f"[bold blue]{versions[0]}[/bold blue]\n")
    else:
        # Multiple versions in table
        table = Table(
            title=f"Available versions for [bold green]{pkg_name}[/bold green] (latest first)",
            show_header=True,
            header_style="bold magenta"
        )
        table.add_column("Version", style="cyan")
        table.add_column("Release Type", style="yellow")
        
        for version in versions:
            # Determine if it's a pre-release, post-release, or final release
            parsed_version = parse_version(version)
            if parsed_version.is_prerelease:
                release_type = "Pre-release"
            elif parsed_version.is_postrelease:
                release_type = "Post-release"
            else:
                release_type = "Final"
            
            table.add_row(version, release_type)
        
        console.print(table)


def main() -> None:
    """Main entry point for the command-line interface."""
    if len(sys.argv) < 2:
        console = Console()
        console.print("[bold red]Error:[/bold red] Package name is required")
        console.print("\n[bold]Usage:[/bold] ppvc <package_name> [--latest]")
        sys.exit(1)
        
    pkg_name = sys.argv[1]
    latest_only = '--latest' in sys.argv[2:]
    
    try:
        versions = get_package_versions(pkg_name, latest_only)
        display_versions(pkg_name, versions)
    except (HTTPError, URLError) as e:
        console = Console()
        console.print(f"[bold red]Error:[/bold red] {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
