"""Test della configurazione."""

from __future__ import annotations

import pytest

from rag.common import ConfigError, load_settings, required


def test_default_quando_ambiente_vuoto(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("RAG_ENVIRONMENT", raising=False)
    monkeypatch.delenv("RAG_LOG_LEVEL", raising=False)

    settings = load_settings()

    assert settings.environment == "local"
    assert settings.log_level == "INFO"
    assert settings.is_local


def test_legge_i_valori_dall_ambiente(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RAG_ENVIRONMENT", "produzione")
    monkeypatch.setenv("RAG_LOG_LEVEL", "debug")

    settings = load_settings()

    assert settings.environment == "produzione"
    assert settings.log_level == "DEBUG"
    assert not settings.is_local


def test_log_level_non_valido(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RAG_LOG_LEVEL", "verboso")

    with pytest.raises(ConfigError, match="LOG_LEVEL"):
        load_settings()


def test_required_su_variabile_assente(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("RAG_KEY_VAULT_URI", raising=False)

    with pytest.raises(ConfigError, match="RAG_KEY_VAULT_URI"):
        required("KEY_VAULT_URI")


def test_required_ignora_gli_spazi(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RAG_KEY_VAULT_URI", "  https://kv.vault.azure.net/  ")

    assert required("KEY_VAULT_URI") == "https://kv.vault.azure.net/"


def test_settings_immutabile(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("RAG_ENVIRONMENT", raising=False)
    settings = load_settings()

    with pytest.raises((AttributeError, TypeError)):
        settings.environment = "altro"  # type: ignore[misc]
