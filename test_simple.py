import pytest
import utils


def test_nom_majuscule():
    assert utils.string_capital('texte') == 'TEXTE'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        utils.string_capital(9)
