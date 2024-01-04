# Weather test case

## Getting Started

To get this project up and running on your local machine, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Tezlaa/test_for_forager_ai.git
   ```
2. **Navigate to the folder**
    ```bash
    cd test_for_forager_ai
    ```
3. **Build and run Docker Container**

    ```bash
    docker-compose build --up
    ```

## Usage

There is a swagger, located at `/api/docs/`

- Register: `accounts/signup/`
- Login: `accounts/login/`
- logout: `accounts/logout/`

#### API:
- `api/v1/current/`: API for getting current weather by user location.
- `api/v1/search/{query}`: API to search for current weather by city name or zip code
- `api/v1/forecast/`: API for getting forecast weather by user's location
- `api/v1/forecast?city_name={}`: getting forecast by GET parametr


## Testing
```bash
python manage.py test apps.weather.tests.test_views
python manage.py test apps.accounts.tests.test_views
```
