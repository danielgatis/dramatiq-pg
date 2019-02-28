from sh import dramatiq_pg


def test_stats():
    out = dramatiq_pg('stats')
    assert 'done: ' in out
