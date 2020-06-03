load(
    "@lambda_deps//:requirements.bzl",
    "requirement"
)

py_binary(
    name = 'calculate_expected_price',
    main = 'expected_price.py',
    srcs = ['expected_price.py'],
    srcs_version="PY3ONLY",
    python_version="PY3",
    deps = [
        requirement('requests'),
        requirement('yfinance'),
        requirement('lxml')
    ]
)
