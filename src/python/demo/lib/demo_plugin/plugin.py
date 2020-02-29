"""Demo pytest plugin"""


class DemoPlugin(object):
    """Sample plugin"""

    def pytest_runtest_logreport(self, report):
        if report.passed:
            print('test passed!')


def pytest_addoption(parser):
    group = parser.getgroup('demo_pants')
    group.addoption(
        '--demo', action='store',
        dest='demo',
    )


def pytest_configure(config):

    if config.getoption('demo'):

        _plugin = DemoPlugin()
        config._demo_plugin = _plugin
        config.pluginmanager.register(config._demo_plugin)


def pytest_unconfigure(config):

    demo_plugin = getattr(config, '_demo_plugin', None)

    if demo_plugin:
        config.pluginmanager.unregister(demo_plugin)
