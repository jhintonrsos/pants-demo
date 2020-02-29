python_library(
    name = "demo_plugin",
    dependencies = [
        "3rdparty/python:pytest-logging",
    ],
    provides = setup_py(
        name = "pytest-demo-plugin",
        description = "Demo plugin",
        entry_points = {
            "pytest11": [
                "demo_plugin = demo.lib.demo_plugin.plugin",
            ],
        },
        license = "no",
        url = "https://github.com",
        version = "1.0.0",
        zip_safe = True,
    ),
    sources = [
        "plugin.py",
        "setup.py",
    ],
)
