import pytest
import sure
from alphabet import LetterFilter


string = "onomatopoeia"
not_asci = "♥O◘♦♥O◘♦"
filter = LetterFilter(string)
outcome_filter_vowel = "ooaooeia"
outcome_filter_consontants = "nmtp"

def test_vowel():
    vowel = filter.filter_vowels()
    assert vowel.should.equal(outcome_filter_vowel)

def test_consonants():
    consonants = filter.filter_vowels()
    assert consonants.should.equal(outcome_filter_vowel)

def test_asci_vowel():
    filter = LetterFilter(not_asci)
    with pytest.raises(ValueError):
        faulty_input = filter.filter_vowels()

def test_asci_consonants():
    filter = LetterFilter(not_asci)
    with pytest.raises(ValueError):
        faulty_input = filter.filter_vowels()
