import sys
import subprocess
import pathlib
import unittest

SCRIPT = pathlib.Path(__file__).parent / "self_printing.py"

class TestSelfPrinting(unittest.TestCase):
    def test_quine(self):
        out = subprocess.run(
            [sys.executable, str(SCRIPT)],
            capture_output=True,
            text=True,
            check=True
        ).stdout
        file_text = SCRIPT.read_text(encoding="utf-8")
        self.assertEqual(out.strip(), file_text.strip())

if __name__ == "__main__":
    unittest.main()
