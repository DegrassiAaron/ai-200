"""Configurazione letta dalle variabili d'ambiente.

Tutte le variabili usano il prefisso ``RAG_``. I valori sensibili non stanno qui:
dalla settimana 12 arrivano da Key Vault, e questo modulo tiene solo il puntatore
alla risorsa che li custodisce.

Aggiungere un'impostazione significa tre cose: un campo in :class:`Settings`, una
riga in :func:`load_settings` e una riga in ``.env.example``.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

PREFIX = "RAG_"

_LIVELLI_LOG = frozenset({"CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"})


class ConfigError(RuntimeError):
    """Una variabile d'ambiente obbligatoria manca o ha un valore non valido."""


def required(nome: str) -> str:
    """Legge ``RAG_<nome>``; solleva :class:`ConfigError` se manca o è vuota."""
    valore = os.environ.get(PREFIX + nome, "").strip()
    if not valore:
        raise ConfigError(f"variabile d'ambiente obbligatoria mancante: {PREFIX}{nome}")
    return valore


def optional(nome: str, default: str = "") -> str:
    """Legge ``RAG_<nome>``, oppure ``default`` se manca o è vuota."""
    return os.environ.get(PREFIX + nome, "").strip() or default


@dataclass(frozen=True, slots=True)
class Settings:
    """Le impostazioni dell'applicazione, immutabili una volta caricate."""

    environment: str
    log_level: str

    @property
    def is_local(self) -> bool:
        return self.environment == "local"


def load_settings() -> Settings:
    """Costruisce :class:`Settings` dall'ambiente corrente.

    :raises ConfigError: se un valore obbligatorio manca o non è valido.
    """
    log_level = optional("LOG_LEVEL", "INFO").upper()
    if log_level not in _LIVELLI_LOG:
        attesi = ", ".join(sorted(_LIVELLI_LOG))
        raise ConfigError(f"{PREFIX}LOG_LEVEL='{log_level}' non valido; attesi: {attesi}")

    return Settings(
        environment=optional("ENVIRONMENT", "local"),
        log_level=log_level,
    )
