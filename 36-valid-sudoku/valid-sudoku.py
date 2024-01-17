class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRow(r) -> bool:
            row = []
            for i in board[r] :
                if i != '.' : row.append(i)
            if len(set(row)) != len(row) :
                return False
            return True
        
        def isCol(c) -> bool:
            col = []
            for i in range(9) :
                if board[i][c] != '.' : col.append(board[i][c])
            if len(set(col)) != len(col) :
                return False
            return True
        
        def isBox(box) :
            box = [b for b in box if b != '.']
            if(len(set(box))) != len(box) :
                return False
            return True

        #row
        for i in range(9) :
            if not isRow(i) : return False
        
        #col
        for i in range(9) :
            if not isCol(i) : return False

        #box
        for i in range(0, 9, 3) :
            for j in range(0, 9, 3) :
                box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if not isBox(box) : return False
        return True