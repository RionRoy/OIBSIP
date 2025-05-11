# OIBSIP
Projects for Oasis Infobyte Internship
This repository contains three Python-based projects developed for the Oasis Infobyte Internship. The projects focus on various aspects of Python programming, including command-line tools, graphical user interfaces (GUIs), and API integrations. Below is an overview of each project, highlighting key concepts, features, and challenges.

1. BMI Calculator
Project Overview
The BMI Calculator is a tool designed to help users calculate their Body Mass Index (BMI) and categorize it based on predefined health standards. The project is developed in two versions:

Basic Version: A command-line interface (CLI) application that prompts users to input their weight (in kilograms) and height (in meters) to calculate their BMI. The application then classifies the result into categories such as underweight, normal weight, and overweight based on standard BMI ranges.

Advanced Version: A GUI-based BMI calculator developed using Tkinter. This version allows users to input their height and weight through an intuitive graphical interface. Additionally, the advanced version includes features such as saving user data, viewing historical BMI records, and generating trends and statistics based on previous BMI calculations.

Key Features:
User Input Validation: Ensures that inputs are within reasonable ranges.

BMI Calculation: Accurate BMI formula calculation.

Categorization: Classifies BMI results into categories like underweight, normal, and overweight.

Graphical Interface (Advanced): Easy-to-use interface with Tkinter for an enhanced user experience.

Data Storage & Trend Analysis (Advanced): Ability to store user data and visualize BMI trends through graphs and charts.

Key Challenges:
Proper input validation to avoid incorrect data.

Categorization based on BMI values, with clear feedback to users.

Implementing data storage and visualizing historical data in an intuitive manner.

2. Random Password Generator
Project Overview
This project provides a random password generator that helps users create strong and secure passwords based on their preferences. It has two versions:

Basic Version: A simple CLI tool that generates a random password based on user-specified criteria, such as password length and character types (letters, numbers, symbols).

Advanced Version: A GUI-based password generator that uses Tkinter. This version enhances the basic functionality by allowing users to customize password complexity, ensure adherence to security rules, and easily copy generated passwords to the clipboard. Users can also exclude certain characters from the generated password if needed.

Key Features:
Randomization: Uses Python’s random module to generate secure passwords.

Customization: Users can choose password length and include/exclude specific character sets.

Security Rules (Advanced): Ensures passwords are complex enough by enforcing rules like the inclusion of both uppercase and lowercase letters, numbers, and symbols.

Clipboard Integration (Advanced): Allows users to copy the generated password to the clipboard for easy use.

Key Challenges:
Managing different character sets for password generation.

Ensuring that the generated passwords meet security best practices.

Designing an intuitive and user-friendly GUI for password generation.

3. Basic Weather App
Project Overview
The Weather App project is a tool for fetching and displaying weather information for a user-specified location. It integrates with a weather API to retrieve data and display it in a user-friendly format. This project has two versions:

Basic Version: A command-line app that asks for a user-specified location (city or ZIP code) and fetches current weather data, such as temperature, humidity, and weather conditions.

Advanced Version: A GUI-based weather app developed using Tkinter. The advanced version allows users to input their location or use automatic GPS detection to get real-time weather information. It provides detailed weather data, including hourly and daily forecasts, wind speed, and temperature units (Celsius/Fahrenheit). The app also displays weather icons and visual elements for an engaging experience.

Key Features:
API Integration: Connects to a weather API to fetch and parse JSON data.

User Input Handling: Handles input validation for the city or ZIP code.

Detailed Weather Data (Advanced): Displays comprehensive weather information such as current conditions, hourly forecasts, wind speed, and temperature units.

GUI Design (Advanced): A polished and responsive user interface that displays weather data clearly and efficiently.

Visual Elements (Advanced): Uses icons and graphical elements to represent weather conditions visually.

Key Challenges:
Proper handling and parsing of API data to retrieve accurate weather information.

Implementing error handling for incorrect user inputs or API failures.

Designing a visually appealing and responsive GUI for displaying weather data.

Conclusion
These projects are designed to improve Python programming skills, with a focus on practical applications such as data validation, GUI design, API integration, and user interaction. The projects are scalable, with beginner-friendly versions as well as more advanced versions that incorporate enhanced features and functionalities.

Feel free to explore the individual projects in this repository. Each project is structured to provide comprehensive learning experiences for anyone looking to deepen their knowledge of Python and software development.


