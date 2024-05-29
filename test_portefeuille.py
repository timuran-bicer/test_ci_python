import pytest
from portefeuille import Portefeuille, ValeurPTFInsuffisante


def test_ptf_valeur_defaut():
    ptf = Portefeuille()
    assert ptf.valeur == 10


def test_ptf_valeur_choisie():
    ptf = Portefeuille(20)
    assert ptf.valeur == 20


def test_ptf_ajouter_argent():
    ptf = Portefeuille(10)
    ptf.ajouter_argent(90)
    assert ptf.valeur == 100


def test_ptf_depenser_argent():
    ptf = Portefeuille(20)
    ptf.depenser_argent(10)
    assert ptf.valeur == 10


def test_depenser_argent_raises_exception_on_valeur_insuffisante():
    ptf = Portefeuille()
    with pytest.raises(ValeurPTFInsuffisante):
        ptf.depenser_argent(100)
