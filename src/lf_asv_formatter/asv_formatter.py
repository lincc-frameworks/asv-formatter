class AsvFormatter:
    """Base class for ASV-specific formatters."""

    MAX_NUM_ROWS = 10
    DEFAULT_OUTPUT_FILE = "output"

    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file if input_file else self.DEFAULT_OUTPUT_FILE
        self.output_file = output_file if output_file else self.DEFAULT_OUTPUT_FILE

    def extract_table_from_file(self):
        """Extracts the asv table content from the output file.

        Returns
        -------
        list of str
            The list of file rows that constitute the asv table.
        """
        with open(self.input_file, "r", encoding="utf-8") as file:
            lines = file.readlines()
            start_index = self.get_table_start_index(lines)
            return lines[start_index:]

    def get_table_start_index(self, lines):
        """Fetches the line index for the start of the table. The table starts
        after the first empty line of the `asv compare` output, and it has a
        3 line banner that should be discarded.

        Parameters
        ----------
        lines: list of str
            The lines of the output file.

        Returns
        -------
        int
            The line index in which the table starts.
        """
        start_index = -1
        i = 0
        while i < len(lines):
            if lines[i].strip() == "":
                # Skip the "All benchmarks" banner
                start_index = i + 3
                break
            i += 1
        if start_index == -1 or start_index >= len(lines):
            raise ValueError("Invalid asv table")
        return start_index

    def write_output_to_file(self, output):
        """Writes the formatted asv table to disk.

        Parameters
        ----------
        output : str
            The formatted asv table.
        """
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write(output)
