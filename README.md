
# Minimal Keyboard Automation

A simple PyQt6-based application for automating keyboard inputs with customizable commands and repetition settings. Designed to execute sequences of keyboard actions efficiently and allow easy configuration through a user-friendly GUI.

---

## Features

- **Customizable Commands**: Enter sequences of commands with delays.
- **Repetition Settings**: Define the number of times the sequence should run (including infinite mode).
- **Special Keys**: Supports special keys like `Ctrl`, `Alt`, `Enter`, and more.
- **File Integration**: Load commands from or save commands to a file.
- **Shortcut Support**: Use the `F12` key to start/stop the script.
- **Always on Top**: Application remains on top of other windows for quick access.

---

## Requirements

- Python 3.7 or higher
- PyQt6
- pynput

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TheCrimsonborn/minimalKeyboardAutomation.git
   cd minimalKeyboardAutomation
   ```

2. **Create a Virtual Environment** (Optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```

---

## Usage

1. **Enter Commands**:
   - Type a sequence of commands (e.g., `a,1,b,2`) in the input field.
   - Odd positions represent keys, and even positions represent delays (in seconds).

2. **Set Repetitions**:
   - Use the spinner to set the number of repetitions.
   - Set to `-1` for infinite repetitions.

3. **Control Execution**:
   - Click the `Start/Stop` button to execute or stop the sequence.
   - Alternatively, press the `F12` key to start or stop.

4. **File Integration**:
   - Save commands to a file for reuse.
   - Load commands from a previously saved file.

---

## Special Keys

Supported special keys are defined in the `keys.json` file. Examples include:
- `alt`
- `ctrl`
- `shift`
- `enter`
- `space`

You can modify or expand this list in the `keys.json` file.

---

## Example

To press `A`, wait 1 second, press `B`, and wait 2 seconds:
```text
a,1,b,2
```

---

## Keyboard Shortcut

- **F12**: Start or stop the automation process.

---

## Development

### Adding Dependencies
To add a new dependency to the project:
1. Install the package:
   ```bash
   pip install <package-name>
   ```
2. Freeze the dependencies:
   ```bash
   pip freeze > requirements.txt
   ```

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **PyQt6** for building the GUI.
- **pynput** for keyboard control.
