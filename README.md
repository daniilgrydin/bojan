# Bojan Library

BojanConsole is a Python library designed to enhance console logging with various message types and color-coded outputs. It also includes a simple progress bar implementation.

## Installation

To install Bojan simply run

```bash
pip install bojan
```

## Syntax Highlight

A [VS Code extension](https://github.com/daniilgrydin/bojan-vscode-highlighter) is available to highlight the .bojan and .bjn log files.

## Usage

### BojanConsole Class

#### Initialization

```python
from bojan import BojanConsole

console = BojanConsole(printing=True)
```

#### Logging Messages

- **Info Message**:
    ```python
    console.log_plain("This is an info message.")
    ```

- **Debug Message**:
    ```python
    console.debug("This is a debug message.")
    ```

- **Error Message**:
    ```python
    console.error("This is an error message.")
    ```

- **Success Message**:
    ```python
    console.success("This is a success message.")
    ```

- **Warning Message**:
    ```python
    console.warning("This is a warning message.")
    ```

#### Printing Dictionaries

```python
sample_dict = {"key1": "value1", "key2": {"subkey1": "subvalue1"}}
console.dictionary(sample_dict)
```

#### Saving Logs

```python
console.save("logfile.txt")
```

#### Initialization

```python
from bojan import ProgressBar

progress_bar = ProgressBar(total=100)
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.