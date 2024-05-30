class LimiteCacahueteAtteinte(Exception):
    pass


class Cacahuete(object):
    def __init__(self, montant_initial=100):
        self.montant = montant_initial

    def manger(self, quantite):
        self.montant -= quantite

    def acheter(self, quantity):
        self.montant += quantity
        if self.montant > 500:
            raise LimiteCacahueteAtteinte("J'ai trop de cacahuete")
