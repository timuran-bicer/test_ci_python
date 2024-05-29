import pytest
from portefeuille import Portefeuille


@pytest.fixture
def mon_ptf():
    """Renvoi un portefeuille avec une valeur par defaut"""
    return Portefeuille()


@pytest.mark.parametrize("gagne,depense,attendu", [
    (30, 10, 30),
    (20, 2, 28),
])
def test_transactions(mon_ptf, gagne, depense, attendu):
    mon_ptf.ajouter_argent(gagne)
    mon_ptf.depenser_argent(depense)
    assert mon_ptf.valeur == attendu
