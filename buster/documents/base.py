from abc import ABC, abstractmethod
from dataclasses import dataclass

import pandas as pd


@dataclass
class DocumentsManager(ABC):
    @abstractmethod
    def add(self, source: str, df: pd.DataFrame):
        """Write all documents from the dataframe into the db as a new version."""
        ...

    @abstractmethod
    def update_source(self, source: str, display_name: str = None, note: str = None):
        """Update the display name and/or note of a source. Also create the source if it does not exist."""
        ...
