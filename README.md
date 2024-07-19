# IP-Subnet-Calculator

This program works as a subnet calculator simular to the website [here](https://www.calculator.net/ip-subnet-calculator.html)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Program-Overview](#program-overview)

## Installation

This project does not require any external pip packages. You only need [Python](https://www.python.org/downloads/) installed on your system.

### Option 1: using [git](https://git-scm.com/downloads)
1. Clone the repository:

    ```sh
    git clone https://github.com/LucasHasting/IP-Subnet-Calculator.git
    ```

2. Navigate to the project directory and execute the program:

    ```sh
    cd IP-Subnet-Calculator
    py subnetting.py
    ```
### Option 2: without git
1. Download the project as a zip file
2. [Extract the zip file](https://www.wikihow.com/Unzip-a-File)
3. In windows, the subnetting.py file can be clicked to execute

#### Run from the command line
1. Find the location of the files
2. Copy the path
3. go to the command line and run the following:
   ```sh
   cd /path/to/files
   py subnetting.py
   ```

## Usage

The program asks the user to enter an IP address and subnet mask in dotted decimal form, and will output the network address, usables range, and the broadcast address.

## Example

For an example of how to use the program, see the video here (to be posted in the future).

## Program-Overview

The [subnetting.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/subnetting.py) file contains the main driver of the program and is what needs to be executed, the [functions_and_constants.py](https://github.com/LucasHasting/IP-Subnet-Calculator/blob/main/functions_and_constants.py) file contains the constants used in both programs and the functions used in subnetting.py
