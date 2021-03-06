from typing import TYPE_CHECKING, cast
from typing import Dict, List, Optional, Union


API_VERSION: str
DEFAULT_AUXWORDS: List[str]
DEFAULT_BANWORDS: List[str]
DEFAULT_BRAINFILE: str
DEFAULT_ORDER: int
DEFAULT_SWAPWORDS: List[str]
DEFAULT_TIMEOUT: float
END_WORD: str
ERROR_WORD: str


class Reply:
    text: str
    levenshtein: float
    surprise: float
    rating: float

    def __init__(self, text: str, levenshtein: float, surprise: float): ...


class Tree:
    children: List[Tree]
    def __init__(self, symbol: int): ...
    def add_symbol(self, symbol: int) -> Tree: ...
    def get_child(self, symbol: int, add: bool) -> Optional[Tree]: ...


class Dictionary(list):
    def add_word(self, word: str) -> int: ...
    def find_word(self, word: str) -> int: ...


class Brain:
    timeout: Union[float, int]
    def __init__(self, order: Optional[int], file: Optional[str], timeout: Union[int, float, None], banwords: Optional[List[str]]): ...
    def init_db(self, clear: bool, order: Optional[int], banwords: Optional[List[str]]): ...
    @property
    def order(self) -> int: ...
    @staticmethod
    def get_words_from_phrase(phrase: str) -> List[str]: ...
    def communicate(self, phrase: str, learn: bool, reply: bool, max_length: Optional[int], timeout: Union[float, int, None]) -> Optional[Reply]: ...
    def get_context(self, tree: Tree) -> Dict: ...
    def learn(self, words: List[str]): ...
    def get_reply(self, words: List[str], max_length: Optional[int], timeout: Union[int, float, None]) -> Optional[Reply]: ...
    def get_replies(self, words: List[str], max_length: Optional[int], timeout: Union[int, float, None]) -> List[Reply]: ...
    def evaluate_reply(self, keys: List[str], words: List[str]) -> float: ...
    def generate_replywords(self, keys: Optional[List[str]]) -> List[str]: ...
    def make_keywords(self, words: List[str]) -> Dictionary: ...


class MegaHAL:
    def __init__(self, order: Optional[int], brainfile: Optional[str], timeout: Optional[int], banwords: Optional[List[str]], banwordfile: Optional[str], max_length: Optional[int]): ...
    @property
    def brainsize(self) -> int: ...
    @property
    def banwords(self) -> List[str]: ...
    @property
    def auxwords(self) -> List[str]: ...
    @property
    def swapwords(self) -> Dict[str, str]: ...
    def train(self, file: str): ...
    def learn(self, phrase: str): ...
    def get_reply(self, phrase: str, max_length: Optional[int], timeout: Union[float, int, None]) -> Optional[Reply]: ...
    def get_reply_nolearn(self, phrase: str, max_length: Optional[int], timeout: Union[float, int, None]) -> Optional[Reply]: ...
    def interact(self, timeout: int): ...
