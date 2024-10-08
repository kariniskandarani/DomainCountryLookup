# DomainCountryLookup
## Table of Contents 
1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Requirements](#requirements)
4. [Usage](#usage)
5. [Code Snippet Image](#code-snippet-image)

## Project Overview
DomainCountryLookup is a Python utility designed to enhance your domain analysis workflows. It allows you to map top-level domains (TLDs) to their corresponding ISO 3166-1 alpha-2 country codes. In addition to this core functionality, the tool processes email data by extracting the user, domain, and country fields, and then appends this information to a converted JSON file for easy access and integration.

## Key Features:
- __TLD to Country Code Mapping__: Effortlessly map TLDs to their corresponding ISO 3166-1 alpha-2 country codes using the *pycountry* library.
- __Email Data Processing__: Extract *user*, *domain*, and *country* information from email addresses contained in the provided CSV file.
- __JSON Conversion__: Automatically convert the processed data into a structured JSON format, adding the extracted fields for streamlined use in various applications.

## Requirements 
- Python 3.x
- pycountry library
- Pandas Library
- CSV file with email data

## Usage 

<!-- Clone the repository -->
```cmd
git clone https://github.com/kariniskandarani/DomainCountryLookup.git
```
<!-- Install Dependencies -->
```cmd
pip install Pandas
```
```cmd
pip install pycountry
```
__Note__: you can use any IDE of your preference. I used google collab.

## Code Snippet Image
<img src="https://github.com/kariniskandarani/DomainCountryLookup/blob/main/CodeSnippet.png" alt="Project Logo" width="700"/>

