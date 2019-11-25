import numpy as np

from mango.domain.domain_space import domain_space


def test_domain():
    params = {
        'a': range(10),
        'b': np.random.randint(0, 1e6, size=50),
        'c': np.random.uniform(low=-100., high=100., size=(50,)),
        'd': [1, 0.1, 2.0],
        'e': ['a', 1, 'b', 'c', None],
        'f': ['1', '-1']
    }
    ds = domain_space(params, domain_size=1000)
    print(ds.mapping_categorical)
    print(ds.mapping_int)
    assert all(k in ds.mapping_int for k in ['a', 'b'])
    assert all(k in ds.mapping_categorical for k in ['c', 'd', 'e', 'f'])
    samples = ds.get_domain()

    for sample in samples:
        for param in params.keys():
            assert (sample[param] in params[param])

