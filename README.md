# Stock Price Expected Move Calculator

## :rocket: Getting started

### <a name="python_code"></a> Setup Python code

#### <a name="python_3"></a> Python 3

Please use Python 3 during development.
Python 3 is pre-installed starting with macOSJazz (10.15).

If your development Mac is running an earlier version of macOS, you can download and install [python-3.7.3-macosx10.9.pkg](https://www.python.org/ftp/python/3.7.3/python-3.7.3-macosx10.9.pkg) (or [later](https://www.python.org/ftp/python/) if available).

#### <a name="python_virtualenv"></a> Python virtual environemnt

After downloading the repo from here, you need to create a virtual environment and install dependencies with `pip`:

1.  Go to the root of the repo: `cd ExpectedMoveCalculator/`

2.  Create a new environemnt

    ```
    ➜  python3 -m venv <name-of-env>
    ```

    We will use `venv` as `<name-of-env>` in this guide

3.  Active virtualenv with

    ```
    ➜  source venv/bin/activate
    ```

    Note: This step is essential and is required to run the consumer.

    When the venv is actiaved, you should be able to see a `(venv)` in front of your command line. For example:

        (venv) ➜  ExpectedMoveCalculator git:(master)

4.  Install all dependencies
    ```
    ➜  pip install -r requirements.txt
    ```

### Running the script

- Params:

  - `-s` or `--stock`: Stock Symbol (e.g. TSLA)
  - `-d` or `--days`: How many days are the option expiration date from today (e.g. 7)

- Example:

To get the expected price for Apple (AAPL) in 7 days:

```
(venv) ➜  ExpectedMoveCalculator git:(master) ✗ python expected_price.py -s AAPL -d 7
Pre close price: 318.25
AAPL IV: 26.0
AAPL expected move is +/- 11.45893743131511
High: 329.7089374313151, Low: 306.7910625686849
```
