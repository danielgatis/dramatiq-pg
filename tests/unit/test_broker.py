from uuid import uuid4


def test_message_lock(monkeypatch, mocker):
    from dramatiq_pg.broker import message_lock

    for _ in range(20):
        message = mocker.Mock(message_id=uuid4(), queue_name='default')
        assert message_lock(message).bit_length() <= 64

    class MockSha256:
        value = None

        def __init__(self, value):
            pass

        def hexdigest(self):
            return self.value

    monkeypatch.setattr('dramatiq_pg.broker.sha256', MockSha256)
    MockSha256.value = '0'*64
    message = mocker.Mock(message_id=uuid4(), queue_name='default')
    assert message_lock(message) == -2**63
    MockSha256.value = 'f'*64
    assert message_lock(message) == 2**63 - 1
