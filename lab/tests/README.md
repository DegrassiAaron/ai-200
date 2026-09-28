# tests

```bash
pytest
```

`test_config.py` è il modello: niente rete, niente Azure, l'ambiente si finge con `monkeypatch`.

Per i componenti che parlano con Azure, tieni separati i test che girano offline da quelli che
richiedono risorse vere — questi ultimi costano, e non devono partire per sbaglio:

```python
@pytest.mark.azure
def test_ricerca_su_cosmos_reale(): ...
```

Registra il marker in `pyproject.toml` sotto `[tool.pytest.ini_options]` ed escludilo per default
con `-m "not azure"`.
