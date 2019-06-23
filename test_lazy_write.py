import time
import unittest
from pathlib import Path

import lazy_write


class MyTestCase(unittest.TestCase):
    def test_lazy_write(self):
        write_path: Path = Path(__file__).parent / 'build' / 'lazy-write-test.file'
        content = str(time.time())

        self.assertTrue(lazy_write.write(write_path, content, parents=True))
        self.assertFalse(lazy_write.write(write_path, content, parents=True))

        content = b'3.26'
        self.assertTrue(lazy_write.write(write_path, content, parents=True))
        self.assertFalse(lazy_write.write(write_path, content, parents=True))


if __name__ == '__main__':
    unittest.main()
