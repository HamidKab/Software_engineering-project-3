"""
Hamid Kabia
003106981
"""

class Trienode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
        node.is_end = True

    def starts_with(self, prefix):
        node = self.root 
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def is_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end   


class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.rows = len(grid)
        self.cols = max(len(row) for row in grid) if grid else 0
        self.dictionary = dictionary
        self.solutions = set()

        self.trie = Trie()
        for word in self.dictionary:
            word_upper = word.strip().upper()
            if len(word_upper) >= 3 and word_upper.isalpha():
                self.trie.insert(word_upper)  
        self._solve()

    def setGrid(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = max(len(row) for row in grid) if grid else 0
        self.solutions = set()
        self._solve()

    def setDict(self, dictionary):
        self.dictionary = dictionary
        self.solutions = set()  
        self.trie = Trie()
        for word in dictionary:
            word_upper = word.strip().upper()
            if len(word_upper) >= 3 and word_upper.isalpha():
                self.trie.insert(word_upper)
        self._solve()  

    def getSolution(self): 
      results = []
      for found_word in self.solutions:
          results.append(found_word.upper()) 
      return sorted(results)

    def _solve(self):
        if not self.grid or self.rows == 0 or self.cols == 0:
            return
        for row in range(self.rows):
            for col in range(len(self.grid[row])):
                visited = [[False] * len(self.grid[r]) for r in range(self.rows)]
                self.dfs(row, col, "", visited, self.trie.root)

    def dfs(self, row, col, current_word, visited, node):
        if row < 0 or row >= self.rows or col < 0 or col >= len(self.grid[row]):
            return

        if visited[row][col]:
            return

        current_tile = self.grid[row][col].upper()

        if current_tile == 'QU':
            char_to_process = 'QU'
        elif current_tile == "ST":
            char_to_process = 'ST'  
        else:
            char_to_process = current_tile

        temp = node
        for char in char_to_process:
            if char not in temp.children:
                return
            temp = temp.children[char]

        next_node = temp
        new_word = current_word + char_to_process

        visited[row][col] = True

        if len(new_word) >= 3 and next_node.is_end:
            self.solutions.add(new_word)

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dx, dy in directions:
            nx, ny = row + dx, col + dy
            if (0 <= nx < self.rows and 0 <= ny < len(self.grid[nx])):
                self.dfs(nx, ny, new_word, visited, next_node)

        visited[row][col] = False


def main():
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"], ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz",
                  "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    found_words = mygame.getSolution()

    print(f"Found words:{found_words}")


    print(f"\nTotal words found: {len(found_words)}")


if __name__ == "__main__":
    main()
