from abc import ABC, abstractmethod
class Animal:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def set_name(self, name: str):
        self._name = name

    def set_age(self, age: int):
        self._age = age

    def name(self) -> str:
        return self._name

    def age(self) -> int:
        return self._age

    @abstractmethod  # Декоратор для абстрактного метода
    def voice(self) -> str:
        pass
