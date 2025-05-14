# Library Management System Database

## Project Description
This is a complete MySQL database for a Library Management System. It handles:
- Book inventory with authors, publishers, and categories
- Member management
- Loan tracking and reservations
- Fine calculations
- Staff management
- System auditing

## Database Schema
The database consists of 11 tables with proper relationships:
- 1-to-Many: Members → Loans, Books → Loans
- Many-to-Many: Books ↔ Authors, Books ↔ Categories
- Self-referencing: Staff → Staff (supervisor hierarchy)

## Setup Instructions
1. Install MySQL Server (version 8.0 or higher recommended)
2. Run the SQL script:
   ```bash
   mysql -u username -p < LibraryManagementSystem.sql
