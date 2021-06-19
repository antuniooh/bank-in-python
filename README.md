<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/antuniooh/bank-in-python">

  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/antuniooh/bank-in-python">
  
  <a href="https://github.com/antuniooh/bank-in-python/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/antuniooh/bank-in-python">
  </a>
  
   <img alt="GitHub" src="https://img.shields.io/github/license/antuniooh/bank-in-python">
</p>

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/antuniooh/bank-in-python">
    <img src="https://i.pinimg.com/originals/b9/c6/2b/b9c62b76602925ded4127ff0df2892c9.png" alt="Logo" width="550">
  </a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-darkblue?style=for-the-badge&logo=python&logoColor=white"/>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#-about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#-how-to-run">How To Run</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## 💻 About The Project
The project consists of software that simulates a bank, performing customer registrations and transactions.

![app](https://github.com/antuniooh/bank-in-python/blob/master/images/app.gif)

The program reads the user-selected text file that contains an adjacency matrix of the graph.

**Option 1** - You can create a new customer at the bank, defining your Name, CPF, type of bank account, the initial amount of your balance and the password that will be used for transactions.

Account types and their specifications: Salary: charges 5% for each debit made Does not allow debits that leave the account with a negative balance

Common: charges 3% fee for each debit made Allows a negative balance of up to (BRL 500.00)

Plus: charges 1% fee for each debit made Allows a negative balance of up to (BRL 5,000.00)

**Option 2** - From the customer's CPF and password, it is possible to remove the customer's bank account.

**Option 3** - From the CPF and password it is possible to debit an amount from the bank account, however it is only executed if the amount is consistent with the available and with the type of account, as each one has a certain predefined credit limit.

**Option 4** - From the CPF and the password it is possible to deposit an amount from the bank account.

**Option 5** - From the CPF and password it is possible to view the current balance of the bank account.

**Option 6** - From the CPF and password, it is possible to view all data relating to bank account transactions.

<!-- HOW TO RUN -->
## 🚀 How To Run

```bash

# Clone the repository
$ git clone https://github.com/antuniooh/bank-in-python.git

# Access the project folder in your terminal / cmd
$ cd bank-in-python

# In both Windows and Linux, the execution is done by executing the following line in the terminal, or using an IDE of your choice.
$ python3 main.py

```