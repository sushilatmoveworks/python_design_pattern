class GreekTranslator:
    def __init__(self) -> None:
        self.translations = {"hello": "Χαίρετε"}

    def translate(self, word: str) -> str:
        return self.translations.get(word, word)

class EnglishTranslator:
    def __init__(self) -> None:
        self.translations = {"hello": "engligh_hello"}

    def translate(self, word: str) -> str:
        return self.translations.get(word, word)

def get_translator(lang="English") -> object:
    translators = {"English": EnglishTranslator, "Greek": GreekTranslator}
    return translators[lang]()

def main():
    """
    >>> e, g = get_translator(lang="English"), get_translator(lang="Greek")
    >>> e.translate(word="hello")
    'engligh_hello'
    >>> g.translate(word="hello")
    'Χαίρετε'
    """

if __name__=='__main__':
    import doctest
    doctest.testmod()
