# Dangerous Writing App

A desktop writing application built with Python and Tkinter. It features an inactivity timer that automatically deletes all written text if the user stops typing for 10 seconds.

## Screenshot

<img width="1470" height="921" alt="Screenshot 2026-11-07 at 3 25 27 PM" src="https://github.com/user-attachments/assets/d1af9aab-9e5a-40f4-b43d-82e1684699e9" />

<img width="1470" height="922" alt="Screenshot 2026-11-07 at 3 26 18 PM" src="https://github.com/user-attachments/assets/62ceb98e-698c-4dff-9203-aecf0f7089b5" />


## Features

- **Inactivity Timer:** Automatically deletes all text after 10 seconds without typing.
- **Live Countdown:** Displays the remaining time during a writing session.
- **Dynamic Color Indicator:** Changes the countdown color based on the remaining time:
  - Green: 7–10 seconds remaining.
  - Orange: 4–6 seconds remaining.
  - Red: 0–3 seconds remaining.
- **Automatic Session Restart:** Typing again starts a new writing session.
- **Multiline Text Editor:** Provides a spacious area for writing.

## Technologies

- Python
- Tkinter
- Time module

## How It Works

The application uses `time.time()` to track the last keyboard input and Tkinter's `after()` method to periodically check the elapsed time.

If no key is pressed for 10 seconds, the application automatically clears the text editor and resets the session.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/gustavodev6331/disappearing-text-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd disappearing-text-app
   ```

3. Run the application:

   ```bash
   python main.py
   ```


## Author

**Gustavo Sene**

[GitHub](https://github.com/gustavodev6331)
