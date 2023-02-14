from sprites.corpoCeleste import CorpoCeleste

class Planeta(CorpoCeleste):
    def __init__(self, x, y, massa):
        super().__init__(x, y, massa)
    
    def atualiza_aceleracao(self, planetas):
        # Calcular a aceleração resultante devido à atração gravitacional dos outros planetas
        self.ax = 0
        self.ay = 0
        for planeta in planetas:
            if planeta != self:
                dx = planeta.x - self.x
                dy = planeta.y - self.y
                dist = ((dx**2 + dy**2)**0.5)
                f = self.massa * planeta.massa / dist**2
                self.ax += f * dx / dist
                self.ay += f * dy / dist