import pytest

import arachide


@pytest.fixture
def cacahuete_default():
    """Renvoie ub objet cacahuete"""
    return arachide.Cacahuete()


@pytest.fixture
def cacahuete_100():
    """Renvoie un objet cacahuete à 100"""
    return arachide.Cacahuete(100)


def test_arachide_quantite_initiale(cacahuete_default):
    assert cacahuete_default.montant == 150


def test_arachide_manger(cacahuete_default):
    cacahuete_default.manger(50)
    assert cacahuete_default.montant == 100


def test_arachide_acheter(cacahuete_default):
    cacahuete_default.acheter(100)
    assert cacahuete_default.montant == 250


def test_arachide_max_achat_500(cacahuete_100):
    cacahuete_100.acheter(400)
    with pytest.raises(arachide.LimiteCacahueteAtteinte):
        cacahuete_100.acheter(50)


@pytest.mark.parametrize("manger,achetter,attendu", [
    (30, 10, 80),
    (100, 2, 2),
])
def test_transactions(cacahuete_100, manger, achetter, attendu):
    cacahuete_100.manger(manger)
    cacahuete_100.acheter(achetter)
    assert cacahuete_100.montant == attendu
