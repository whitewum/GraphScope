import networkx.algorithms.operators.tests.test_unary
import pytest

from graphscope.experimental.nx.utils.compat import import_as_graphscope_nx

import_as_graphscope_nx(networkx.algorithms.operators.tests.test_unary,
                        decorators=pytest.mark.usefixtures("graphscope_session"))
