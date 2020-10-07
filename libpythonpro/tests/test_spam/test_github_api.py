from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = "https://avatars1.githubusercontent.com/u/48964182?v=4"
    resp_mock.json.return_value = {
        "login": "GetulioCastro",
        "id": 48964182,
        "avatar_url": url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('GetulioCastro')
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('GetulioCastro')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('GetulioCastro')
    assert 'https://avatars1.githubusercontent.com/u/48964182?v=4' == url
