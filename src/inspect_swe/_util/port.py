"""Process-global port allocator for sandbox model proxies.

Each concurrent sample needs a unique port for its model proxy server.
The inspect_ai Store is backed by a ContextVar (per-sample), so using
it for port allocation causes every concurrent sample to independently
compute the same port.  This module provides a process-global counter
that guarantees uniqueness across all concurrent samples.
"""

import itertools

_port_counter = itertools.count(13131)


def allocate_port() -> int:
    """Return the next unique port number.

    Safe to call from any async task or thread within the process.
    Ports are never reused within a single process lifetime.
    """
    return next(_port_counter)
