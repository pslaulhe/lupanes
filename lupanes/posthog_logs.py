"""Isolated OpenTelemetry log export for PostHog-authored application logs."""

import atexit
import logging

from django.conf import settings

_configured = False


def configure_posthog_log_export() -> None:
    """Export only records emitted through the dedicated PostHog logger."""
    global _configured

    if _configured or not settings.POSTHOG_MW_CLIENT:
        return

    from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
    from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
    from opentelemetry.sdk._logs.export import BatchLogRecordProcessor

    logger_provider = LoggerProvider()
    exporter = OTLPLogExporter(
        endpoint=f"{settings.POSTHOG_HOST.rstrip('/')}/i/v1/logs",
        headers={"Authorization": f"Bearer {settings.POSTHOG_PROJECT_TOKEN}"},
    )
    logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))

    posthog_logger = logging.getLogger("lupanes.posthog_logs")
    posthog_logger.addHandler(LoggingHandler(logger_provider=logger_provider))
    posthog_logger.setLevel(logging.INFO)
    posthog_logger.propagate = False

    atexit.register(logger_provider.shutdown, 3000)
    _configured = True
