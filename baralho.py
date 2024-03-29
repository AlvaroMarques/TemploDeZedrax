import chess

class Piece:
    def __init__(self, piece, board):
        self.piece = [str(piece)]
        self.board = board

    def temPeca(self):
        return self.board.piece_at(self.dest)

    def move(self):
        aux = self.board.copy()
#         print(self.piece)
        for i in range(len(self.piece)):
#             print(self.piece)
            if(str(self.piece[i]).upper() == 'P'):
                num = 1
            elif(str(self.piece[i]).upper() == 'N'):
                num = 2
            elif(str(self.piece[i]).upper() == 'B'):
                num = 3
            elif(str(self.piece[i]).upper() == 'R'):
                num = 4
            elif(str(self.piece[i]).upper() == 'Q'):
                num = 5
            elif(str(self.piece[i]).upper() == 'K'):
                num = 6
            
            mov = chess.Move(self.ini, self.ini, num)
            aux.push(mov)
#             print(self.board)
            mov = chess.Move.null()
            aux.push(mov)
            mov = chess.Move(self.ini, self.dest)
            #self.aux.push(mov)
            if(mov in aux.legal_moves):
#                 print(self.ini)
#                 print(self.dest)
                self.board.push(mov)
#                 print(self.board)
                return True
#             mov = chess.Move(self.ini, self.dest)
#             if(mov in self.board.legal_moves):
#                 self.board.push(mov)
        

    def set_ini(self, ini):
        self.ini = ini

    def set_dest(self, dest):
        self.dest = dest

    def get_ini(self):
        return self.ini

    def atualizaBoard(self, board):
        self.board = board

class Jogo:
    def __init__(self):
        self.vet = []
        self.comidos = []
        self.board = chess.Board()
        self.acabou = 0
        for a in range(16):
            self.vet.append(Piece(self.board.piece_at(a), self.board))
            self.vet[a].set_ini(a)
        for b in range(48, 64):
            a = a+1
            self.vet.append(Piece(self.board.piece_at(b), self.board))
            self.vet[a].set_ini(b)
#         for i in range(len(self.vet)):
#              print(self.vet[i].get_ini())
    def lsum(self, l):
            a = []
            for i in l:
                a += i
            return a
    def atualizaPosicao(self):
#         print(self.board)
        aux = str(self.board.copy())
        k = self.lsum([n.split() for n in aux.split("\n")[::-1]])

        d = {}
        for i, peca in enumerate(k):
            if peca != ".":
                d[i] = peca
        a = 0
        for k in d:
#             print(k)
#             print(d[k])
            self.vet[a] = Piece(d[k], self.board)
            self.vet[a].set_ini(k)
            a = a+1
    def movimenta(self, ini, dest):
        k=0
#         print("movimenta")
        for i in self.vet:
            #print(i.get_ini())
            if(int(i.get_ini()) == (ini)):
                #print(i.get_ini())
                break
            k = k+1
        #print(k)
        self.vet[k].set_dest(dest)
        #print(atual.piece)
        if(self.vet[k].temPeca()):
            self.comidos.append(str(self.vet[k].temPeca()))
            capturada = self.vet[k].temPeca()
            if capturada not in self.vet[k].piece:
                self.vet[k].piece.append(str(capturada))
        self.vet[k].move()
        self.vet[k].set_ini(dest)
        self.mate()

        
        
    def get_board(self):
        return self.board
    def mate(self):
        aux = str(self.board.copy())
        if('k' not in self.lsum([n.split() for n in aux.split("\n")[::-1]])):
            self.acabou =  1
        if('K' not in self.lsum([n.split() for n in aux.split("\n")[::-1]])):
            self.acabou =  2
    def retorno_final(self):
        checkmate = "nao"
        if(self.acabou == 1):
            checkmate = "branco"
        if(self.acabou == 2):
            checkmate = "preto"
        dic = {
            "board": str(self.board),
            "check_mate": checkmate
        }
        return dic
        
        


