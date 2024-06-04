Installations:
pip install selenuim
pip install pytest
pip install pytest-xdist - for parallel testing 

Runing tests:
python -m pytest tests- all tests
python -m pytest tests/your-test-name.py - specific test
python -m pytest tests -n {number of jobs to run the tests} - running parallel tests
