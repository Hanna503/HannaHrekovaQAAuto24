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
    assert r['total_count'] == 58
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
    status_code = github_api.get_emoji('1f947.png?v8')
    assert status_code == 200


@pytest.mark.api
def test_emoji_not_exists(github_api):
    status_code = github_api.get_emoji('11111a.png?v8')
    assert status_code == 404


@pytest.mark.api
def test_commit_not_exists(github_api):
    owner = 'octocat'
    repo = 'Hello-World'
    commit_sha = 'commit_not_exists'
    commit = github_api.get_commit(owner, repo, commit_sha)
    assert commit['message'] == 'Not Found'