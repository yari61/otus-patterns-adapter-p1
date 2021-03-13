from __future__ import annotations

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Factory

from .summarize import Summarize, SummarizePairFactory, SummarizePair
from matrix_sum.matrix import MinimalMatrixFactory


class SummarizeContainer(DeclarativeContainer):
    config = Configuration()
    matrix_factory = Factory(MinimalMatrixFactory)
    summarize_pair_factory = Factory(SummarizePairFactory, matrix_factory=matrix_factory)
    summarize = Factory(Summarize, matrices=config.matrices, summarize_pair_factory=summarize_pair_factory)

__all__ = ["SummarizeContainer"]
