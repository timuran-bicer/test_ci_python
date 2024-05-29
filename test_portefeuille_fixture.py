import pytest
from portefeuille import Portefeuille, ValeurPTFInsuffisante


@pytest.fixture
def ptf_defaut():
    """Renvoi un portefeuille avec une valeur par defaut"""
    return Portefeuille()


@pytest.fixture
def ptf():
    """Renvoi un portefeuille avec une valeur à 20"""
    return Portefeuille(20)


def test_ptf_valeur_defaut(ptf_defaut):
    assert ptf_defaut.valeur == 10


def test_ptf_valeur_choisie(ptf):
    assert ptf.valeur == 20


def test_ptf_ajouter_argent(ptf):
    ptf.ajouter_argent(90)
    assert ptf.valeur == 110


def test_ptf_depenser_argent(ptf):
    ptf.depenser_argent(10)
    assert ptf.valeur == 10


def test_depenser_argent_raises_exception_on_valeur_insuffisante(ptf_defaut):
    with pytest.raises(ValeurPTFInsuffisante):
        ptf_defaut.depenser_argent(100)


@pytest.mark.parametrize("gagne,depense,attendu", [
    (30, 10, 30),
    (20, 2, 28),
])
def test_transactions(gagne, depense, attendu):
    mon_ptf = Portefeuille()
    mon_ptf.ajouter_argent(gagne)
    mon_ptf.depenser_argent(depense)
    assert mon_ptf.valeur == attendu
