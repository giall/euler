from unittest import TestLoader, TextTestRunner

loader = TestLoader()
suite = loader.discover('src')

runner = TextTestRunner()
runner.run(suite)