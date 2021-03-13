from __future__ import annotations

from .cli import parser
from .input import FileLoadContainer
from .operations import SummarizeContainer
from .output import DumpContainer

if __name__ == "__main__":
    load_container = FileLoadContainer()
    summarize_container = SummarizeContainer()
    dump_container = DumpContainer()

    args = parser.parse_args()
    load_container.config.set("path", args.input)
    loader = load_container.loader()
    matrices = loader()

    summarize_container.config.set("matrices", matrices)
    summarize = summarize_container.summarize()
    result_matrix = summarize()

    dump_container.config.set("path", args.output)
    dump_container.config.set("matrix", result_matrix)
    dumper = dump_container.dumper()
    dumper()
