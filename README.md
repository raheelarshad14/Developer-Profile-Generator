# Developer Profile Generator

#### Video Demo: <https://youtu.be/yun0rShcmG4?si=1tksIYNIC0H8YaMC>

#### Description:

Developer Profile Generator is a Python application that analyzes a public GitHub profile using the GitHub REST API. The user enters a GitHub username, and the program retrieves the user's profile information and public repositories.

It processes the retrieved data to calculate:
- Total public repositories
- Total GitHub stars
- Programming language usage
- Top five repositories based on stars

The results are displayed in the terminal and exported to both `Resume.json` and `Resume.md`. The report also includes the date and time it was generated.

The project is divided into small functions, each responsible for a single task such as fetching user data, retrieving repositories, calculating statistics, exporting files, and displaying the final report. This modular design makes the code easier to understand, test, and maintain.

For testing, I used `pytest` to verify the core functions responsible for language statistics, total star calculation, and repository sorting.

This project helped me gain practical experience working with REST APIs, JSON data, dictionaries, lists, file handling, Markdown generation, and writing clean, modular Python code.
