from abc import ABC, abstractmethod


class AbstractShyObject(ABC):
    @abstractmethod
    def _get_items(self) -> dict:
        pass

    @abstractmethod
    def unveil(self) -> dict:
        pass

    @abstractmethod
    def veil(self) -> dict:
        pass


class ShyObject(AbstractShyObject):
    def __init__(self, **kwargs) -> None:
        self._private = False
        self._keys = []
        [self.__setattr__(key, value) for key, value in kwargs.items()]

    def __getitem__(self, item) -> str:
        if self._private:
            return 'Hidden'
        return getattr(self, item)

    def __setitem__(self, key, value) -> None:
        self.__setattr__(key, value)

    def __setattr__(self, key, value) -> None:
        if '_' not in key:
            self._keys.append(key)
        super(ShyObject, self).__setattr__(key, value)

    def _get_items(self) -> dict:
        return {key: self[key] for key in self._keys}

    def unveil(self) -> dict:
        self._private = False
        return self._get_items()

    def veil(self) -> dict:
        self._private = True
        return self._get_items()


a = ShyObject(a=1, b=2)
a['c'] = 3
print(a.unveil())
print(a.veil())