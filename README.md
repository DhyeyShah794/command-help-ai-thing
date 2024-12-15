# Command Help AI Thing (C.H.A.T.)

Command Help AI Thing (C.H.A.T.) is a command-line AI assistant designed to help you with terminal commands, file operations, and general queries. It provides customizable responses using different model engines.

---

## Features

- **Ask Questions:** Get detailed instructions for terminal operations and general queries.
- **Customizable Engines:** Choose from a variety of AI models for tailored responses.
- **Adjustable Randomness:** Fine-tune the creativity level of responses.
- **Command History:** Review past queries and responses, with options for detailed views.

---

## Getting Started

### Basic Usage
To ask a question:

```bash
python main.py ask "<Query>"
```
Example:
```bash
python main.py ask "How to delete a file named test.txt in the Documents folder?"
```
Output:
```
To delete a file named "test.txt" in the Documents folder on Linux, you can use the `rm` command in the terminal. Here are the steps to follow:
1. Open the terminal application on your Linux system.
2. Navigate to the Documents folder by typing `cd ~/Documents` and pressing Enter.
3. Type the following command to delete the "test.txt" file:
   `rm test.txt`
4. Press Enter to execute the command.
```

---

### Change Engine
Choose an AI model to generate responses. Available engines:
- Ada (`text-ada-001`)
- Babbage (`text-babbage-001`)
- Curie (`text-curie-001`)
- Davinci (`text-davinci-003`)

Usage:
```bash
python main.py ask "<Query>" --engine "<engine-name>"
```
Example:
```bash
python main.py ask "How to delete a file named test.txt in the Documents folder?" --engine "text-ada-001"
```

---

### Adjust Randomness
Control the creativity of responses by setting a randomness value between 0 (least creative) and 1 (most creative).

Usage:
```bash
python main.py ask "<Query>" --randomness <value>
```
Example:
```bash
python main.py ask "How to delete a file named test.txt in the Documents folder?" --randomness 0.2
```

---

### Command History

#### Show Last 10 Queries (Default)
View the last 10 queries and responses:
```bash
python main.py history
```

#### Show Last n Queries
Specify the number of past queries to display:
```bash
python main.py history <n>
```

#### Detailed History
View detailed history with additional information like engine, randomness, and timestamp:
```bash
python main.py history <n> --detailed true
```
Example:
```bash
python main.py history 1 --detailed true
```
Output:
```
Q1: How to delete a file named test.txt in the Documents folder?
Answer:
To delete a file named "test.txt" in the Documents folder on Linux, you can use the `rm` command in the terminal. Here are the steps to follow:
1. Open the terminal application on your Linux system.
2. Navigate to the Documents folder by typing `cd ~/Documents` and pressing Enter.
3. Type the following command to delete the "test.txt" file:
   `rm test.txt`
4. Press Enter to execute the command.

Engine: text-davinci-003
Randomness: 0.5
Timestamp: 2023-03-24 15:43:36
```

---

## Requirements
- Python 3.7 or higher

---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/DhyeyShah794/command-help-ai-thing.git
```
2. Navigate to the project directory:
```bash
cd command-help-ai-thing
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

---

## Contact
For questions or feedback, feel free to reach out at [your-email@example.com].
