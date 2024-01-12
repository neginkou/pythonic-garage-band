import pytest
from pythonic_garage_band.band import Band, Musician, Guitarist, Bassist, Drummer

@pytest.fixture
def one_band():
    members = [
        Guitarist("Kurt Cobain"),
        Bassist("Krist Novoselic"),
        Drummer("Dave Grohl"),
    ]
    some_band = Band("Nirvana", members)
    return some_band

def test_guitarist_str():
    joan = Guitarist("Joan Jett")
    actual = str(joan)
    expected = "My name is Joan Jett and I play guitar"
    assert actual == expected

def test_guitarist_repr():
    joan = Guitarist("Joan Jett")
    actual = repr(joan)
    expected = f"Guitarist instance. Name = {joan.name}"
    assert actual == expected

def test_drummer_str():
    sheila = Drummer("Sheila E.")
    actual = str(sheila)
    expected = "My name is Sheila E. and I play drums"
    assert actual == expected

def test_drummer_repr():
    sheila = Drummer("Sheila E.")
    actual = repr(sheila)
    expected = f"Drummer instance. Name = {sheila.name}"
    assert actual == expected

def test_bassist_str():
    meshell = Bassist("Meshell Ndegeocello")
    actual = str(meshell)
    expected = "My name is Meshell Ndegeocello and I play bass"
    assert actual == expected

def test_bassist_repr():
    meshell = Bassist("Meshell Ndegeocello")
    actual = repr(meshell)
    expected = f"Bassist instance. Name = {meshell.name}"
    assert actual == expected

def test_band_name():
    nirvana = Band("Nirvana", [])
    assert nirvana.name == "Nirvana"

def test_guitarist():
    jimi = Guitarist("Jimi Hendrix")
    assert jimi.name == "Jimi Hendrix"
    assert jimi.get_instrument() == "guitar"

def test_bassist():
    flea = Bassist("Flea")
    assert flea.name == "Flea"
    assert flea.get_instrument() == "bass"

def test_drummer():
    ginger = Drummer("Ginger Baker")
    assert ginger.name == "Ginger Baker"
    assert ginger.get_instrument() == "drums"

def test_instruments(one_band):
    instruments = ["guitar", "bass", "drums"]
    for i, member in enumerate(one_band.members):
        assert member.get_instrument() == instruments[i]

def test_individual_solos(one_band):
    for member in one_band.members:
        if member.get_instrument() == "guitar":
            assert member.play_solo() == "face melting guitar solo"
        elif member.get_instrument() == "bass":
            assert member.play_solo() == "bom bom buh bom"
        elif member.get_instrument() == "drums":
            assert member.play_solo() == "rattle boom crash"

def test_band_members(one_band):
    assert len(one_band.members) == 3

    assert isinstance(one_band.members[0], Musician)
    assert isinstance(one_band.members[0], Guitarist)
    assert one_band.members[0].name == "Kurt Cobain"

    assert isinstance(one_band.members[1], Musician)
    assert isinstance(one_band.members[1], Bassist)
    assert one_band.members[1].name == "Krist Novoselic"

    assert isinstance(one_band.members[2], Musician)
    assert isinstance(one_band.members[2], Drummer)
    assert one_band.members[2].name == "Dave Grohl"

def test_class_tracks_instances():
    assert Band.to_list() == []
    the_nobodies = Band("The Nobodies", [])
    all_bands = Band.to_list()
    assert len(all_bands) == 1
    assert all_bands[0] == the_nobodies

@pytest.fixture(autouse=True)
def clean():
    Band.instances = []
