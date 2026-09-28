"""Punto di ingresso: carica la configurazione e la stampa.

Serve a verificare che l'ambiente sia impostato bene, in locale e dentro il container::

    python -m rag
    docker run --rm --env-file .env rag-lab
"""

from __future__ import annotations

import logging
import sys

from rag import __version__
from rag.common import ConfigError, load_settings


def main() -> int:
    try:
        settings = load_settings()
    except ConfigError as errore:
        print(f"configurazione non valida: {errore}", file=sys.stderr)
        return 1

    logging.basicConfig(
        level=settings.log_level,
        format="%(asctime)s %(levelname)-8s %(name)s %(message)s",
    )
    log = logging.getLogger("rag")
    log.info("rag-lab %s avviato", __version__)
    log.info("environment=%s log_level=%s", settings.environment, settings.log_level)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
