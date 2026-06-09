# Beautiful Calc (A-pro-Calculator-in-python)

A clean, beginner-friendly console-based calculator written in Python. It runs in an interactive loop, performs mathematical operations, and automatically builds into a standalone Windows `.exe` using GitHub Actions.

## Features

- **Operations Supported:**
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`) with division-by-zero protection
  - Square Root (unary operation)
- **Continuous Loop:** Runs continuously so you can make multiple calculations.
- **Clean Menu UI:** Shows the menu banner once at start.
- **Input Validation:** Gracefully handles non-numeric inputs without crashing.
- **CI/CD Build:** Uses Nuitka to bundle the project into a single `.exe` file.

## How to Run Locally

Make sure you have Python 3 installed. Run the following command in your terminal:

```bash
python main.py
```

## How to Download the Windows EXE

You can download the pre-compiled `.exe` file directly from GitHub:

1. Go to the **Actions** tab of this repository.
2. Select the latest successful run of the **Build Windows EXE** workflow.
3. Scroll down to the **Artifacts** section at the bottom.
4. Download the `windows-exe` ZIP file, extract it, and run `main.exe`.
