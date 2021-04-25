import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        print("known_mines", self.mines)
        return self.mines

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        print("known_safes", self.safe)
        return self.safe

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # print("mark_mine", cell)
        # self.mines.add(cell)
        # print(self.mines)
        """for sentence in self.knowledge:
            for cells in sentence:
                for cell in cells:
                    print(sentence, cells, cell)"""

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        
        # print(self, cell)
        # print(self.cells)
        # print(self.count)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)
    
    def neighbors(self, cell):
        neighbors = []
        # print(cell)
        # Loop over all cells within one row and column
        # print(cell)
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):
                # Ignore the cell itself
                if (i, j) == cell or i < 0 or j < 0 or i > 7 or j > 7:
                    continue
                neighbors.append((i, j))
        return neighbors
    
    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        print("1) marked the cell as a move that has been made")
        self.moves_made.add(cell) # 1) mark the cell as a move that has been made
        print("2) marked the cell as safe")
        self.mark_safe(cell) # 2) mark the cell as safe
        
        print("knowledge", self.knowledge)
        print("3) added a new sentence to the AI's knowledge base")
        sentence = Sentence([cell], count)
        # print(sentence)
        self.knowledge.append(sentence)
        
        print("knowledge", self.knowledge)
        
        # sentence = Sentence([cell], count)
        # print("Sentence", sentence)
        # self.knowledge.append(sentence) # 3) add a new sentence to the AI's knowledge base
            
        """
        for sentence in self.knowledge: # 4) mark any additional cells as safe or as mines
            # print(sentence)
            # print(sentence.count)
            if sentence.count == 0:
                cells = sentence.cells
                for cell in cells:
                    # print(cell)
                    # print(self.neighbors(cell))
                    neighbors = self.neighbors(cell)
                    # print(neighbors)
                    for cell in range(len(neighbors)): 
                        self.mark_safe(neighbors[cell])
        """                
        
        # print(cell)
        neighbors = self.neighbors(cell)
        # print(neighbors)
        sentence = Sentence(neighbors, count)
        # print(sentence)
        self.knowledge.append(sentence)
        # print(self.knowledge)
        
        for sentence in self.knowledge:
            print(sentence)        
            for cell in sentence.cells: 
                # print(cell)"""                    
                if sentence.count == 0: self.mark_safe(cell)
                #if sentence.count != 0:
        
        # 5) add any new sentences to the AI's knowledge base
        
        print("moves_made ", self.moves_made) 
        
        sentence_nr = 0
        for sentence in self.knowledge:
            sentence_nr += 1
            print(sentence_nr, sentence)
            if sentence.count != 0:
                print(sentence.cells.difference(self.moves_made))
                sentence.cells.difference_update(self.moves_made)
                print("sentence without moves_made",sentence)
                if str(sentence.cells).count("(") == sentence.count:
                    for cell in sentence.cells:
                        print("this is a mine", cell)
                        self.mark_mine(cell)
                if str(sentence.cells).count("set()") == 1:
                    self.knowledge.remove(sentence)
                    print("sentence removed")
        for sentence in self.knowledge:
            if str(sentence.cells).count("(") == 1:
                self.knowledge.remove(sentence)
                print("sentence removed")
        
        """
        if count == 0: 
            print("safe neighbors")
            neighbors = []
            # Loop over all cells within one row and column
            for i in range(cell[0] - 1, cell[0] + 2):
                for j in range(cell[1] - 1, cell[1] + 2):
                    # Ignore the cell itself
                    if (i, j) == cell or i < 0 or j < 0 or i > 7 or j > 7:
                        continue
                    self.mark_safe((i, j))
        elif count == 1: None
        elif count == 2: None
        elif count == 3: None
        elif count == 4: None
        elif count == 5: None
        elif count == 6: None
        elif count == 7: None
        elif count == 8: None
        else: None
        """
        
        print("self.mines",self.mines)
        print("self.safes",self.safes)
        print("self.moves_made",self.moves_made)
        
    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        
        safe_move = self.safes.difference(self.moves_made)
        # print("safe_move", safe_move)
        if safe_move.__len__() > 0:
            return  safe_move.pop()
        else:
            return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        not_a_mine = False
        if str(self.moves_made).count("(") == 56:
            return None
        else:
            while not_a_mine == False:
                y = str(random.randint(0,self.height - 1))
                x = str(random.randint(0,self.width - 1))
                if str(self.mines).count(str("("+y+", "+x+")")) == 0 and str(self.moves_made).count(str("("+y+", "+x+")")) == 0:
                    not_a_mine = True
            # print("make_random_move", y, x)
            return (int(y), int(x))
