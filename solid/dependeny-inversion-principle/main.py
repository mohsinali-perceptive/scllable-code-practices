"""
The Dependency Inversion Principle (DIP) is a principle in object-oriented design that states that "High-level modules should not depend on low-level modules. Both should depend on abstractions". means "Big parts of your program should not directly depend on small, detailed parts. Instead, both should depend on general ideas (interfaces)".
"""

from enum import Enum
from abc import ABC, abstractmethod


class IVersionControl(ABC):
    @abstractmethod
    def commit(self, message: str):
        pass

    @abstractmethod
    def pull(self):
        pass

    @abstractmethod
    def push(self):
        pass


class Git(IVersionControl):
    def commit(self, message: str):
        print("commiting using git -> ", message)

    def pull(self):
        print("pulling using git")

    def push(self):
        print("pushing using git")


class Developer:
    def __init__(self, version_control: IVersionControl):
        self.version_control = version_control

    def make_commit(self, message: str):
        self.version_control.commit(message)

    def make_pull(self):
        self.version_control.pull()

    def make_push(self):
        self.version_control.push()


if __name__ == "__main__":
    git = Git()
    developer = Developer(git)
    developer.make_commit("feat: initial commit")
    developer.make_pull()
    developer.make_push()
