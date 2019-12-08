import sys
from random import randint, random


class Obfuscator:

    def __init__(
            self,
            min_length: int,
            max_length: int,
    ) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def obfuscate(
            self,
            command: str
    ) -> str:
        obfuscations = []
        length = randint(self.min_length, self.max_length)
        for _ in range(length):
            if random() > 0.5:
                obfuscations.append('AND')
                obfuscations.append(self._generate_and_clause())
            else:
                obfuscations.append('OR')
                obfuscations.append(self._generate_or_clause())

        obfuscations.insert(0, command)
        return ' '.join(obfuscations)

    def _generate_and_clause(self) -> str:
        num = randint(0, 9)
        return str(num) + '=' + str(num)

    def _generate_or_clause(self) -> str:
        left = randint(0, 1000)
        right = left + randint(1, 1000)
        return str(left) + '=' + str(right)


if __name__ == '__main__':
    obf = Obfuscator(5, 10)
    command = sys.argv[1]
    print(obf.obfuscate(command))
