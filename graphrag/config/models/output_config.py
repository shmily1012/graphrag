# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Parameterization settings for the default configuration."""

from pydantic import BaseModel, Field

import graphrag.config.defaults as defs
from graphrag.config.enums import OutputType


class OutputConfig(BaseModel):
    """The default configuration section for Output."""

    type: OutputType = Field(
        description="The output type to use.", default=defs.OUTPUT_TYPE
    )
    base_dir: str = Field(
        description="The base directory for the output.",
        default=defs.OUTPUT_BASE_DIR,
    )
    connection_string: str | None = Field(
        description="The storage connection string to use.", default=None
    )
    container_name: str | None = Field(
        description="The storage container name to use.", default=None
    )
    storage_account_blob_url: str | None = Field(
        description="The storage account blob url to use.", default=None
    )
    cosmosdb_account_url: str | None = Field(
        description="The cosmosdb account url to use.", default=None
    )
