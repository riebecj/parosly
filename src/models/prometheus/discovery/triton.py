from pydantic import BaseModel, Field

from src.models.prometheus.misc.tls import TLSConfig


class TritonSDConfig(BaseModel):
    """
    Triton SD configurations allow retrieving scrape targets from Container Monitor discovery endpoints.
    ref: https://prometheus.io/docs/prometheus/latest/configuration/configuration/#triton_sd_config
    """

    account: str = Field(..., description="The account to use for discovering new targets.")
    role: str | None = Field(
        "container",
        description="The type of targets to discover. 'container' to discover VMs, 'cn' to "
        "discover compute nodes. Default is 'container'.",
    )
    dns_suffix: str = Field(..., description="The DNS suffix which should be applied to target.")
    endpoint: str = Field(
        ...,
        description="The Triton discovery endpoint (e.g. 'cmon.us-east-3b.triton.zone'). "
        "This is often the same value as dns_suffix.",
    )
    groups: list[str] | None = Field(
        None,
        description="A list of groups for which targets are retrieved, only supported when role is "
        "'container'. If omitted, all containers owned by the requesting account are scraped.",
    )
    port: int | None = Field(9163, description="The port to use for discovery and metric scraping. Default is 9163.")
    refresh_interval: str | None = Field(
        "60s", description="The interval which should be used for refreshing targets. Default is 60 seconds."
    )
    version: int | None = Field(1, description="The Triton discovery API version. Default is 1.")
    tls_config: TLSConfig | None = Field(None, description="TLS configuration settings.")
