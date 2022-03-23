from app import load_json
import pytest


def test_load_json():
    with pytest.raises(ValueError):
        load_json('tests/files/musics.txt')


