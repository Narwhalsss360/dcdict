from dataclasses import is_dataclass, asdict

class DCDict:
    def __iter__(self):
        if not is_dataclass(self):
            raise TypeError(f'{DCDict} child must be a dataclass')
        return iter(asdict(self).items())
