class ValeurPTFInsuffisante(Exception):
    pass


class Portefeuille(object):

    def __init__(self, montant_initial=10):
        self.valeur = montant_initial

    def depenser_argent(self, prix):
        if self.valeur < prix:
            raise ValeurPTFInsuffisante('Valeur du portefeuille insuffisante pour ce prix {}'.format(prix))
        self.valeur -= prix

    def ajouter_argent(self, montant):
        self.valeur += montant
