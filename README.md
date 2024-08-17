# Admit Card Form

This project is a web-based application that allows users to submit their admit card details, including a passport photo and a signature. The application validates the uploaded images, ensuring the correct placement of the photo and signature, and then stores the data in a PostgreSQL database.

## Features

- **User-Friendly Form**: Users can input their personal information, upload a passport photo, and a signature through a simple form.
- **Image Validation**: The backend verifies whether the uploaded images are correctly assigned to the passport photo and signature fields. If the images are misplaced, they are automatically swapped to the correct fields.
- **Data Storage**: The validated data, including the images, are securely stored in a PostgreSQL database.

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python with OpenCV for image processing
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

## Installation

### Prerequisites

- Docker
- Docker Compose

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/admit-card-form.git
   cd admit-card-form
2. Build and run the Docker containers:
    ```bash
   docker-compose up --build

### Usage
- Open the application in your browser.
- Fill in your first name, last name, student ID, email, and date of birth.
- Upload your passport photo and signature.
- Submit the form.
- The backend will verify the images and, if necessary, swap them to the correct fields.
- The data is then stored in the PostgreSQL database.