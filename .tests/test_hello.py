"""Public feedback tests for PS1. Run from the repository root."""
import ast
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
STARTER = 'greeting = "Hello"\nname = "World"\ngreeting = greeting + name\nprint(greeting)\n'


class HelloTests(unittest.TestCase):
    def test_edit_scope(self):
        """5 points: change only the string assigned to name."""
        tree = ast.parse((ROOT / 'hello.py').read_text(encoding='utf-8'))
        expected = ast.parse(STARTER)
        self.assertEqual(len(tree.body), 4, 'Keep the four original statements.')
        assignment = tree.body[1]
        self.assertIsInstance(assignment, ast.Assign, 'Keep the assignment to name.')
        self.assertIsInstance(assignment.value, ast.Constant, 'Assign a string literal to name.')
        self.assertIsInstance(assignment.value.value, str, 'name must be a string.')
        self.assertNotEqual(assignment.value.value, 'World', 'Change the string assigned to name.')
        assignment.value = expected.body[1].value
        self.assertEqual(ast.dump(tree), ast.dump(expected),
                         'Change only the string assigned to name; keep the other code.')

    def test_output(self):
        """5 points: exact output, including spaces and punctuation."""
        try:
            result = subprocess.run([sys.executable, str(ROOT / 'hello.py')],
                                    cwd=ROOT, capture_output=True, text=True, timeout=5)
        except subprocess.TimeoutExpired:
            self.fail('hello.py must finish within five seconds.')
        self.assertEqual(result.returncode, 0, f'Fix the Python error:\n{result.stderr}')
        self.assertEqual(result.stderr, '', 'The program should not produce error output.')
        self.assertEqual(result.stdout, 'Hello World!\n',
                         'Print exactly Hello World! on one line. Check spaces and punctuation.')


if __name__ == '__main__':
    unittest.main()
