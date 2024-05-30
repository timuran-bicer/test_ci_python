import pytest
import utils


def test_string_en_capitale():
    assert utils.string_capital('abc') == 'ABC'


def test_chiffre_en_capital_erreur():
    with pytest.raises(TypeError):
        utils.string_capital(2)


def test_division():
    assert utils.divide(4, 2) == 2


def test_divsision_par_0():
    with pytest.raises(ZeroDivisionError):
        utils.divide(2, 0)


def test_nom_majuscule():
    assert utils.string_capital('texte') == 'TEXTE'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        utils.string_capital(9)


def test_string_to_array_tableau_egal_1():
    tableau = utils.string_to_array('TEXTE')
    assert tableau[0] == 'TEXTE'
    assert len(tableau) == 1


def test_string_to_array_first_string_empty():
    tableau = utils.string_to_array(',TEXTE')
    assert tableau[0] == ''
    assert tableau[1] == 'TEXTE'
    assert len(tableau) == 2


def test_string_to_array_attribute_error():
    with pytest.raises(AttributeError):
        tableau = utils.string_to_array(1425)


def test_return_1_equals_1():
    assert utils.return_1() == 1
