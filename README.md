# GreatReads

This project is a web application that allows users to view books, submit reviews, and browse through other user reviews. It utilizes a **MongoDB** database for data storage, **Java and Spring Boot** for the backend, and **React** for the frontend.

## Technologies Used
- **Backend**: Java, Spring Boot
- **Frontend**: React.js
- **Database**: MongoDB
- **API**: RESTful API
- **UI Components**: React-Bootstrap, Material UI


https://github.com/user-attachments/assets/3bbe1419-a651-401e-8b59-bafefb5b2c7d


## Features
- **Book Listing**: Users can view a list of books.
- **Book Detail**: Users can view detailed information about a specific book.
- **Review Submission**: Users can submit a review for a book.
- **View Reviews**: Users can browse and read reviews submitted by others.
  
## Installation

### Prerequisites
- **Node.js**: Required for running the frontend.
- **MongoDB**: Required for storing book and review data.
- **Java 11+**: Required for running the backend server.

### Setting up the Backend
1. Clone the backend repository:
   ```bash
   git clone <your-backend-repository-url>

## API Endpoints

### `GET /api/v1/books`
- Retrieves a list of all books in the database.

### `GET /api/v1/books/{title}`
- Retrieves details of a specific book, including its reviews.

### `POST /api/v1/reviews`
- Submit a review for a specific book.
