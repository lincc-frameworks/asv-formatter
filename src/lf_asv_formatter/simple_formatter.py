from .asv_formatter import AsvFormatter


class SimpleFormatter(AsvFormatter):
    """The SimpleFormatter is used for asv >= 0.6.0.

    It extracts the table from the ASV output file, clipping it to the maximum
    specified size. The table keeps its original GitHub styling.

    Typical ASV table file (before processing):

    All benchmarks:

    | Change   | Before [bd9dfcb0]    | After [65151fad]    | Ratio   | Benchmark (Parameter)              |
    |----------|----------------------|---------------------|---------|------------------------------------|
    |          | 2.67±0.3s            | 4.05±0.2s           | ~1.52   | benchmarks.TimeSuite.time_xrange   |
    |          | 1.97±1s              | 2.51±0.9s           | ~1.27   | benchmarks.TimeSuite.time_keys     |
    |          | 2.82±1s              | 1.95±0.8s           | ~0.69   | benchmarks.TimeSuite.time_iterkeys |
    | +        | 464                  | 3.89k               | 8.38    | benchmarks.MemSuite.mem_list       |
    |          | 3.00±0.5s            | 2.97±1s             | 0.99    | benchmarks.TimeSuite.time_range    |

    The output will be similar to:
    | Change   | Before [bd9dfcb0]    | After [65151fad]    | Ratio   | Benchmark (Parameter)              |
    |----------|----------------------|---------------------|---------|------------------------------------|
    |          | 2.67±0.3s            | 4.05±0.2s           | ~1.52   | benchmarks.TimeSuite.time_xrange   |
    |          | 1.97±1s              | 2.51±0.9s           | ~1.27   | benchmarks.TimeSuite.time_keys     |
    |          | 2.82±1s              | 1.95±0.8s           | ~0.69   | benchmarks.TimeSuite.time_iterkeys |
    | +        | 464                  | 3.89k               | 8.38    | benchmarks.MemSuite.mem_list       |
    |          | 3.00±0.5s            | 2.97±1s             | 0.99    | benchmarks.TimeSuite.time_range    |
    """

    def __init__(self, input_file=None, output_file=None):
        super().__init__(input_file, output_file)

    def rewrite_file(self):
        """Reads ASV table and writes new file with transformed table."""
        rows = self.extract_table_from_file()
        output = self.format_asv_table_from_file(rows)
        self.write_output_to_file(output)

    def format_asv_table_from_file(self, rows):
        """Parses the table generated by `asv compare`, and clips the number of
        results to the maximum size, specified by MAX_NUM_ROWS.

        Parameters
        ----------
        rows : list of str
            List of asv table rows.

        Returns
        -------
        str
            The formatted asv table.
        """
        bench_data = rows[2:]
        max_row = min(self.MAX_NUM_ROWS, len(bench_data)) + 2
        return "".join(map(str, rows[:max_row]))
