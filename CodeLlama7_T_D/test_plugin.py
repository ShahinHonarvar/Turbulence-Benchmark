# https://stackoverflow.com/questions/72277284/retrieve-pytest-results-programmatically-when-run-via-pytest-main
class TestResults:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.xfailed = 0
        self.skipped = 0


    def pytest_terminal_summary(self, terminalreporter):
        self.passed = len(terminalreporter.stats.get('passed', []))
        self.failed = len(terminalreporter.stats.get('failed', []))
        self.xfailed = len(terminalreporter.stats.get('xfailed', []))
        self.skipped = len(terminalreporter.stats.get('skipped', []))