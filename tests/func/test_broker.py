from random import randint

import pytest

from example import writer


@pytest.mark.timeout(8)
def test_massive(listener, pgconn, flush_witness):
    count = 32

    # Start listening for ack.
    with listener:
        # Then queue <count> random messages.
        for _ in range(count):
            writer.send(
                randint(1, 10),
                named=randint(1, 10),
            )

        # Wait for 32 ack from workers.
        listener.wait(count)

    # Ensure the witness table has effectively
    with pgconn() as curs:
        curs.execute("SELECT count(*) FROM dramatiq.queue;")
        witness_count, = curs.fetchone()
    assert count == witness_count
