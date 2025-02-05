# SpellCheckerApp

A simple and interactive command-line spell checker application built in Python using the `spellchecker` library. This tool helps users correct misspelled words efficiently.

## 🚀 Features
- ✅ Automatically detects and corrects misspelled words.
- ✅ Displays corrections for incorrect words.
- ✅ User-friendly command-line interface.
- ✅ Allows users to exit the application gracefully.
- ✅ Lightweight and easy to use.

## 📥 Installation

To set up and run the SpellCheckerApp, follow these steps:

### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```
If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### Steps
1. **Clone this repository:**
   ```sh
   git clone https://github.com/your-username/spellchecker-app.git
   cd spellchecker-app
   ```
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```sh
   pip install pyspellchecker
   ```

## 🔹 Usage

Run the script using:
```sh
python spell_checker.py
```

### How It Works
1. The program prompts the user to enter a sentence.
2. It checks for spelling mistakes and suggests corrections.
3. Displays the corrected sentence.
4. Users can exit by typing `q`.

### 📌 Example
#### **Input:**
```
Enter the text (q for exit): Ths is a smple txt
```
#### **Output:**
```
Converting Ths to This
Converting smple to sample
Converting txt to text
Corrected text = This is a sample text
```

## 🛠️ Code Overview
- **`SpellCheckerApp` class:** Handles text correction.
- **`correct_text()` method:** Checks and corrects each word in the input.
- **`mainRun()` method:** Runs the application loop, taking user input.
- **Command-line interaction:** Continuously takes user input and provides corrections until the user exits.

## 🛠 Troubleshooting
If you encounter issues:
- Ensure you have installed `pyspellchecker` using `pip install pyspellchecker`.
- Run the script in an active Python environment.
- Check if you are using Python 3+.

## 🤝 Contributing
We welcome contributions! Feel free to fork this repository, make improvements, and submit a pull request. Here’s how you can contribute:
1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine.
   ```sh
   git clone https://github.com/your-username/spellchecker-app.git
   ```
3. **Create a new branch** for your feature or bug fix.
   ```sh
   git checkout -b feature-branch-name
   ```
4. **Make your changes and commit them.**
   ```sh
   git add .
   git commit -m "Describe your changes here"
   ```
5. **Push to your fork and submit a pull request.**
   ```sh
   git push origin feature-branch-name
   ```

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 📧 Contact
For any questions or feedback, feel free to reach out:
- **GitHub:** [Your Profile](https://github.com/code-with-shahzaib)
- **Email:** codewithshahzaib@gmail.com

## 👤 Author
**Muhammad Shahzaib**

