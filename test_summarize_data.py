import numpy as np
import pandas as pd
import seaborn as sns
import unittest

class summarizeTest(unittest.TestCase):
    def test_summarize_input(self)-> :
        self.assertTrue(
            type(self) == pd.DataFrame
        )
