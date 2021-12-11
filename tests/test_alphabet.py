import pytest
import sure
from alphabet import LetterFilter

filter = LetterFilter()
string = "onomatopoeia"
not_asci = "♥O◘♦♥O◘♦"

outcome_filter_vowel = "ooaooeia"
outcome_filter_consontants = "nmtp"

def test_vowel():
    vowel = filter.filter_vowels(string)
    assert vowel.should.equal(outcome_filter_vowel)

def test_consonants():
    consonants = filter.filter_vowels(string)
    assert consonants.should.equal(outcome_filter_vowel)

def test_asci_vowel():
    with pytest.raises(ValueError):
        faulty_input = filter.filter_vowels(not_asci)

def test_asci_consonants():
    with pytest.raises(ValueError):
        faulty_input = filter.filter_vowels(not_asci)
