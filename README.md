# ProjectRanker

## Overview

ProjectRanker is a command-line interface (CLI) system that recommends and ranks project ideas based on user preferences. It processes user queries, extracts relevant keywords, and matches them against a dataset of project ideas to generate a ranked list of the most relevant projects.

The system uses a score-based ranking engine to determine how well each project aligns with the user's input.

This project is built with a focus on modular design and separation of responsibilities across different files.

---

## Features

- Interactive CLI for user input
- Keyword-based query processing
- Difficulty mapping system
- Tag-based matching
- Score-based ranking algorithm
- Top-N project recommendations
- Modular architecture with separated responsibilities

---

## How It Works

1. User enters project preferences (e.g., python, beginner, machine learning)
2. Input is processed into keywords
3. Dataset is scanned for matches in:
   - Description
   - Tags
   - Difficulty level
4. Each project is assigned a relevance score:
   - Description match → +3
   - Tags match → +4
   - Difficulty match → +2
5. Projects are sorted based on score
6. Top matching projects are displayed

---

## Project Structure

ProjectRanker/
│
├── main.py          # Entry point (CLI interface)
├── manager.py       # Handles user input and sorting logic
├── scorer.py        # Scoring engine
├── project.csv      # Dataset containing project ideas
├── README.md        # Project documentation
└── requirements.txt # Dependencies

---

## Installation

Clone the repository:

git clone https://github.com/username/ProjectRanker.git
cd ProjectRanker

Install dependencies:

pip install -r requirements.txt

---

## Usage

Run the application:

python main.py

Example input:

Enter your Query: python beginner machine learning

---

## Output

The system returns the top matching projects sorted by relevance score.

Example:

====================================
MATCH RESULTS
====================================

Project A
Project B
Project C

---

## Design Principles

- Separation of concerns (each module has a single responsibility)
- Clean modular architecture
- Simple scoring system
- CLI-based interaction
- Extensible structure for future upgrades

---

## Future Improvements

- Weighted scoring system tuning
- NLP-based keyword matching
- Larger dataset expansion
- Web interface version
- ML-based ranking system

---

## Tech Stack

- Python
- Pandas
- Regex (re)
- CLI application

---

## Author

Built as a learning project focused on Python, data processing, and modular system design.