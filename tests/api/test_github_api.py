import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 25
    assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0



@pytest.mark.api
def test_emoji_exists(github_api):
    r = github_api.get_emoji('aries')
    assert r['message'] == 'Found'



@pytest.mark.api
def test_emoji_not_exists(github_api):
    r = github_api.get_emoji('green_cat')
    assert r['message'] == 'Not Found'



@pytest.mark.api
def test_update_name(github_api):
    r = github_api.patch_user('Octocat')
    assert r['message'] == 'Updated'



@pytest.mark.api
def test_location(github_api):
    r = github_api.get_location('San Francisco')
    assert r['message'] == 'Found'