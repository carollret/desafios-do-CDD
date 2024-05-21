class Pessoa:
    def __init__(self):
        self.status = None  # Inicialmente, a pessoa não está fazendo nenhuma atividade.
    def falar(self):
        if self.status == 'comendo':
            print("Não pode falar enquanto está comendo.")
        elif self.status == 'dormindo':
            print("Não pode falar enquanto está dormindo.")
        else:
            self.status = 'falando'
            print("Está falando.")
    def comer(self):
        if self.status == 'falando':
            print("Não pode comer enquanto está falando.")
        elif self.status == 'dormindo':
            print("Não pode comer enquanto está dormindo.")
        else:
            self.status = 'comendo'
            print("Está comendo.")
    def dormir(self):
        if self.status == 'falando':
            print("Não pode dormir enquanto está falando.")
        elif self.status == 'comendo':
            print("Não pode dormir enquanto está comendo.")
        else:
            self.status = 'dormindo'
            print("Foi dormir.")
