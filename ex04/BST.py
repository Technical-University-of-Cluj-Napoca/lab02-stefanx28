# ex04/BST.py
import urllib.request
from typing import List, Optional

class Node:
    def __init__(self, word: str):
        self.word: str = word
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class BST:
    def __init__(self, source: str, **kwargs):
        self.root: Optional[Node] = None
        self._load_words(source, **kwargs)

    def _load_words(self, source: str, **kwargs) -> None:
        url = kwargs.get('url', False)
        file = kwargs.get('file', False)
        if url and file:
            raise ValueError("cannot have both url and file TRUE")
        raw: List[str] = []
        if url:
            with urllib.request.urlopen(source) as resp:
                raw = resp.read().decode('utf-8').splitlines()
        else:
            with open(source, 'r', encoding='utf-8') as f:
                raw = f.read().splitlines()
        words = [w.strip().lower() for w in raw if w.strip().isalpha()]
        words = sorted(set(words))
        self.root = self._build_balance(words, 0, len(words) - 1)

    def _build_balance(self, words: List[str], low: int, high: int) -> Optional[Node]:
        if low > high:
            return None
        mid = (low + high) // 2
        node = Node(words[mid])
        node.left = self._build_balance(words, low, mid - 1)
        node.right = self._build_balance(words, mid + 1, high)
        return node

    def autocomplete(self, prefix: str) -> List[str]:
        res: List[str] = []
        prefix = prefix.lower()
        self._collect(self.root, prefix, res)
        return res

    def _collect(self, node: Optional[Node], prefix: str, res: List[str]) -> None:
        if node is None:
            return
        if node.word < prefix:
            self._collect(node.right, prefix, res)
            return
        if node.word <= prefix:
            self._collect(node.left, prefix, res)
        self._collect(node.left, prefix, res)
        if node.word.startswith(prefix):
            res.append(node.word)
        self._collect(node.right, prefix, res)