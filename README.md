# Building a Currency Converter in Python

## Description
This Python project, which uses the **Streamlit** framework, is a web-based **Currency Converter App**. The application uses real-time exchange rates retrieved from the [Frankfurter](https://www.frankfurter.app/) API to enable users to convert between two chosen currencies. The **latest conversion rate** or the rate for a particular day in the past can be obtained by users when they choose two currencies and enter the amount they wish to convert. Additionally, the **inverse conversion rate** for the selected currencies is provided by the program. The webapp  displays a validation error if the user selects any future date. If the same currency is chosen in both the input fields of conversion, another validation message is displayed. In the event that the input rate is not equal to zero, the program will determine the inverse rate and round it to four decimal places. Hence, the application allows the users to:

- Decide which currencies they wish to exchange.
- Enter the amount that needs to be changed.
- Use the Frankfurter API to retrieve the most recent conversion rates.
- Examine past conversion rates for a certain historical period.
- See the inverse conversion rate, or the rate at which the target currency is converted back to the original.

The app's real-time functionality is one of its main advantages, making it a helpful resource for anyone who need precise and fast currency conversions, including businesses, investors, and travellers.

### Challenges Faced:
- **API data handling:** Managing situations in which the API gives the most recent rate that is available, but the rate date is not today, and putting in place appropriate error handling for when the API is not accessible.
- **Validation for amounts:** Verifying that the user does not submit a negative amount to be converted is the purpose of the validation for amounts.
- **Currency validation:** The conversion's input fields cannot contain the same currency.
- **Validation for historical dates:** Making sure that when a user queries past date, they are unable to choose a date in the future.
- **Retrieval of currency list:** Accurately retrieving and presenting the list of currencies that are available from the API.
- **Real-Time Data Handling:** Keeping a responsive user interface while managing real-time data for both historical and current currency rates.


### Future Features to implement:
- **Graphical Representation of Historical Rates:** Incorporating graphical elements to show exchange rate trends over time, such as a bar graph or line chart. This would make it simpler for consumers to comprehend historical or latest data by giving them a visual depiction of how currency values change.
- **Time Series Conversion for a Date Range:** Users can only choose one historical date at a time at this moment. A more thorough examination of currency movements might be possible with a future update that lets users select a range of dates and see currency conversions across that time frame.
- **Currency conversion for multiple currencies:** The application can currently convert between two currencies simultaneously. Allowing users to choose multiple currencies (e.g., convert USD to EUR, GBP, and AUD all at once) would be a future addition. Users that need to examine rates across multiple currencies at once would find this especially helpful.
- **Using Cached Data in Offline Mode:** Putting in place an offline mode that saves the most recent rates. This would enable the software to continue running even in the event of an internet outage, albeit at somewhat antiquated rates.
- **Alerts on Exchange Rates:** A function that lets users program warnings to sound when exchange rates reach a predetermined level. Users who wish to keep an eye on advantageous rates and base their selections on market fluctuations may find this helpful.
- **Support for several languages and localisation:** Increasing the app's usefulness by localising currency names and symbols according to the user's location and supporting numerous languages.
- **User Authentication and Saved Preferences:** Enabling users to register and store the currencies and conversions they use most frequently. For frequent app users, this would simplify the user experience.
- **User Interface:** Enhancing the user interface by including more exchange rate visualisation over time.

With plenty of opportunity for additional improvements and sophisticated features, this project showcases the usage of APIs for real-time data fetching and a straightforward yet functional web interface utilising Streamlit.


## How to Setup
The following steps should be followed to set up the development environment needed to run this project:

### Prerequisites:
- Python 3.9 or higher
- An active internet connection for fetching live exchange rates from the API

### Setup:
1. **Clone the repository:**
   ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory:**
    ```bash
    cd currency-converter-app
    ```

3. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. **Install the required packages:**

    Install the project dependencies using the following commands:
    ```bash
    pip install streamlit requests
    pip install --upgrade jinja2
    pip install --upgrade numexpr
    pip install --upgrade bottleneck
    ```
### Required Packages and Versions:
- `streamlit==1.22.0` (Web framework for creating the UI)
- `requests==2.31.0` (For making API calls)
- `jinja2==3.1.2` or higher (To support Template Inheritance)
- `numexpr==2.8.4` or higher (For better cache utilization)
---

## Python Version
This project was developed using Python 3.9.


## How to Run the Program
To run the Currency Converter app, follow these steps:
1. Verify all dependencies are installed using the instructions in the **Setup** section.
2. Run the Streamlit application using the following command:
    ```bash
    streamlit run app.py
    ```
3. Once the server starts and the application is running, a web page will automatically open in the default browser. If it does not, open the browser and navigate to `http://localhost:8501`. This link will also be provided in the terminal.

### Example:
##### User Inputs:
- Enter an amount to convert (e.g., 50).
- Select "From Currency" and "To Currency" (e.g., `AUD` to `USD`).
- Click **Get Latest Rate** to see the latest conversion rate.
- Alternatively, select a past date and click **Conversion Rate** to get a rate from that specific date.

The user provided date for the *Latest* and *Historical* will be displayed in the output. If the date falls in a weekend, it will take the closest week day rate from the api call.

## Project Structure

```
dsp_at2_25238736/
│
├── api.py          
├── app.py         
├── frankfurter.py 
├── currency.py    
└── README.md    
```


### Explanation of Files:
1. **`app.py`:** The Streamlit web application is operated by this primary file. It manages user inputs and generates the user interface (UI), using functions specified in other files to retrieve data from the Frankfurter API. The user's view of the results is likewise managed by this file. Python framework `streamlit`, and `datetime` module, along with the functions from the files `frankfurter` and `currency` have been imported here.

    - **Key Functionalities:**
        - **User Interface (UI):** The file builds the interactive user interface (UI) allowing the user to enter data (amount, from and to currencies, date) using Streamlit components such as date pickers, buttons, select boxes, and number inputs.
        - **Fetching Currency List:** The list of supported currencies is retrieved from `frankfurter.py` using `get_currencies_list()` and shown in a dropdown menu when the program is launched.
        - **Fetching Latest Rates:** The `get_latest_rates()` function is invoked to retrieve the current conversion rate for the chosen currencies and amount when the user hits the `Get Latest Rate` button.
        - **Fetching Historical Rates:** When a user clicks on the button **Conversion Rate** after choosing a date, the application executes `get_historical_rate()` to retrieve the conversion rate for that particular date.
        - **User Input Validation:** When the user chooses a future date for historical conversions, the application verifies that the date is correct and displays an error notice if it is not.

    - **Usability**: The entire user interaction flow is controlled by this file. It serves as a link between the backend (API and utility functions) and the frontend (UI). Within this file, every component from other modules cooperates to guarantee that the application runs smoothly and offers a flawless user experience.


2. **`api.py`:** The logic for responding to API queries is contained in this file. It is in charge of managing the responses and sending HTTP GET requests to the Frankfurter API. HTTP client library `requests` has been imported in this file.

    - **Key Functionalities:**
        - Contains the function `get_url(url: str)` that abstracts the process of making API calls. This utility is used throughout the project to interact with the Frankfurter API. It returns the response content and status code after sending an HTTP GET request to the supplied URL. If the status code 200 is returned, the API call is successful and the outputs are displayed for the conversion. `Requests`, an HTTP client library is imported in this file.

    - **Usability:** Other modules communicate with the Frankfurter API through this function. This feature makes sure that any problems with API communication are managed centrally by routing all API calls (for currency lists, the most recent rates, and historical rates).


3. **`frankfurter.py`:** The fundamental features for using the Frankfurter API are provided by this file. It specifies functions that retrieve information such the most recent conversion rates, accessible currencies, and historical conversion rates. `datetime` and `json` modules are imported in this file, along with `get_url` function from the `api` Python file.

    - **Key Functionalities:**
        - `get_currencies_list()`:
            - Retrieves the Frankfurter API's list of available currency codes.
            - Returns a list of currency codes or, in the event that the data fetch failed, None.
        - `get_latest_rates(from_currency, to_currency, amount)`:
            - Retrieves from the Frankfurter API the most recent exchange rate between two currencies.
            - Returns two values: the conversion rate itself and the date of the most recent rate; if an error occurs, it returns None.
        - `get_historical_rate(from_currency, to_currency, from_date, amount)`:
            - Retrieves the exchange rate from the Frankfurter API for a given date.
            - Returns the conversion rate for the specified date or, in the event of a mistake, None.
    - **Usability:** The foundation of the application's currency conversion features are these features. They guarantee that users receive correct and up-to-date information by enabling the app to dynamically retrieve and show the most recent and historical currency rates.

4. **`currency.py`:** Utility functions for processing exchange rates and structuring output for display are included in this file. Rounding rates, inverse rate calculations, and producing readable text output are just a few of the tedious duties made easier by these methods.

    -  **Key Functionalities:**
        - `round_rate(rate)`: Improves readability and accuracy by rounding a floating-point exchange rate to four decimal places.
        - `reverse_rate(rate)`: 
            - Determines an exchange rate's inverse (for example, converting from USD to EUR when EUR to USD is specified).
            - Returns the inverse rate, rounded to 4 decimal places. If the provided rate is zero, it returns 0 to avoid division errors.

        - `format_output(date, from_currency, to_currency, rate, amount)`: 
            - Creates a user-readable string from the currency conversion results.
            - The original rate, the amount in the target currency, and the inverse rate are all included in the output.
    - **Usability:** By standardising the way results are shown in the Streamlit interface, these capabilities let users easily comprehend the output. For example, the application utilises these functions to format the response before displaying it to the user after retrieving the conversion rate.

5. **`README.md`:**
    - The documentation file containing the description of the web application, listing all the implemented Python functions, and instructions for running the web application.


---

## Citations
- Frankfurter API: This project makes use of the [Frankfurter API](https://www.frankfurter.app/docs/), an open-source API for retrieving currency conversion rates.
- Streamlit Documentation: The web app has been built using [Streamlit](https://docs.streamlit.io/) to create an easy-to-use web interface.
