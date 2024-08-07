# CICD_Demo

This project is a simple counter application with a backend built using FastAPI and a frontend built using Angular.

## Project Structure

## Backend

The backend is built using FastAPI and is located in the `counter-app-backend` directory.

### Running the Backend

1. Navigate to the `counter-app-backend` directory.
2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Run the FastAPI application:
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

### API Endpoints

- `GET /counter`: Returns the current value of the counter.
- `POST /counter/increment`: Increments the counter by 1.
- `POST /counter/decrement`: Decrements the counter by 1.
- `POST /counter/reset`: Resets the counter to 0.

## Frontend

The frontend is built using Angular and is located in the `counter-app-frontend` directory.

### Development Server

1. Navigate to the `counter-app-frontend` directory.
2. Install the required dependencies:
    ```sh
    npm install
    ```
3. Run the development server:
    ```sh
    ng serve
    ```
4. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

### Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

### Running Unit Tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

### Running End-to-End Tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Docker

Both the backend and frontend have Docker support.

### Building and Running the Backend Docker Image

1. Navigate to the `counter-app-backend` directory.
2. Build the Docker image:
    ```sh
    docker build -t counter-app-backend .
    ```
3. Run the Docker container:
    ```sh
    docker run -p 8000:8000 counter-app-backend
    ```

### Building and Running the Frontend Docker Image

1. Navigate to the `counter-app-frontend` directory.
2. Build the Docker image:
    ```sh
    docker build -t counter-app-frontend .
    ```
3. Run the Docker container:
    ```sh
    docker run -p 4200:80 counter-app-frontend
    ```

## Further Help

For more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.