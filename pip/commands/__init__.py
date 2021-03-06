"""
Package containing all pip commands
"""


from pip.commands.bundle import BundleCommand
from pip.commands.completion import CompletionCommand
from pip.commands.freeze import FreezeCommand
from pip.commands.help import HelpCommand
from pip.commands.search import SearchCommand
from pip.commands.show import ShowCommand
from pip.commands.install import InstallCommand
from pip.commands.uninstall import UninstallCommand
from pip.commands.unzip import UnzipCommand
from pip.commands.zip import ZipCommand


commands = {
    BundleCommand.name: BundleCommand,
    CompletionCommand.name: CompletionCommand,
    FreezeCommand.name: FreezeCommand,
    HelpCommand.name: HelpCommand,
    SearchCommand.name: SearchCommand,
    ShowCommand.name: ShowCommand,
    InstallCommand.name: InstallCommand,
    UninstallCommand.name: UninstallCommand,
    UnzipCommand.name: UnzipCommand,
    ZipCommand.name: ZipCommand,
}


def get_summaries(ignore_hidden=True):
    """Return a sorted list of (command name, command summary)."""
    items = []

    for name, command_class in commands.items():
        if ignore_hidden and command_class.hidden:
            continue

        items.append((name, command_class.summary))

    return sorted(items)


def get_similar_commands(name):
    """Command name auto-correct."""
    from difflib import get_close_matches

    close_commands = get_close_matches(name, commands.keys())

    if close_commands:
        guess = close_commands[0]
    else:
        guess = False

    return guess
