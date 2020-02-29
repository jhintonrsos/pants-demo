# pants-demo

Pytest plugin which adds simple `--demo` flag, that when paassed to pytest will print test passed! if a test passes

##### TODO
- enable plugin when running pytest via pants

<br>


### Local development without pants
to be able to run something like `pytest -vv hello_world/tests/test_greeting.py --demo`

run `cd src/python && python3 setup.py develop`

<br>

### Integrating pytest plugin with pants 

Run tests, showing how to include extra pytest plugins at runtime (How do we include our local demo plugin?)

```bash
./pants  test  src/python/demo/hello_world/tests:test_greeting --pytest-pytest-plugins=pytest-html==1.22.0
```

<br>

Build local sdist and wheel
```bash
./pants setup-py --recursive src/python/demo/lib/demo_plugin:demo_plugin --setup-py-run="sdist bdist_wheel"
```
