---

# Amazon Price Tracker with Email Alerts 🚨

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green)  
![SMTP](https://img.shields.io/badge/Email-SMTP-orange)

Track prices of Amazon products and get instant email alerts when prices drop below your target! Built with Python, BeautifulSoup, and SMTP.

---

## Features ✨

- **Real-Time Price Tracking**: Scrape product prices from Amazon.
- **Email Notifications**: Get alerts via Gmail when prices fall below your desired threshold.
- **Currency Handling**: Automatically handles Indian price formatting (e.g., `₹5,249` → `5249.00`).
- **Configurable**: Easily set your target price and product URL.

---

## How It Works ⚙️

1. Scrapes the product page using **BeautifulSoup**.
2. Extracts the price and converts it to a float (handling commas for Indian currency).
3. Sends an email via **SMTP** if the current price is below your predefined `BUY_PRICE`.

---

## Installation 📦

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/amazon-price-tracker.git
   cd amazon-price-tracker
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Set Up Credentials**:
   - Create a `credentials.py` file in the same directory with:
     ```python
     EMAIL_ADDRESS = "your_email@gmail.com"
     EMAIL_PASSWORD = "your_app_specific_password"  # Use Gmail App Password
     ```

4. **Run the Script**:
   ```bash
   python main.py
   ```

---

## Usage 🖥️

1. **Configure Settings**:
   - Set `BUY_PRICE` in `main.py` (e.g., `BUY_PRICE = 5000`).
   - Replace the `URL` with your target Amazon product link.

2. **Run the Script**:
   - The script will check the price and send an email if it drops below your threshold.

---

## Configuration 🔧

| Variable          | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `BUY_PRICE`       | Your desired price threshold (e.g., `5250`).                               |
| `URL`             | Amazon product URL to track.                                               |
| `headers`         | HTTP headers to mimic a browser request (prevents blocking).               |
| `EMAIL_ADDRESS`   | Your Gmail address (set in `credentials.py`).                              |
| `EMAIL_PASSWORD`  | Gmail App Password (enable 2FA and generate in Google Account Settings).   |

---

## Example Email 📧

*Sample email alert sent by the script.*

![Screenshot from 2025-02-07 10-03-15](https://github.com/user-attachments/assets/383ac13f-3170-4e17-900a-9311335c66c2)
"Web Scarping for the details"
![Screenshot from 2025-02-07 10-03-55](https://github.com/user-attachments/assets/20cd5376-9ca9-4321-8953-b62d50864d7b)


---

## Dependencies 📚

- `requests` - For HTTP requests.
- `beautifulsoup4` - For HTML parsing.
- `smtplib` - For sending emails (built-in Python library).

---

## Notes ⚠️

- **Amazon Anti-Scraping**: Amazon may block frequent requests. Use responsibly!
- **Gmail Security**: Enable "Less Secure Apps" or use an App Password for SMTP.

---

## Contributing 🤝

Feel free to:
- Add support for multiple products.
- Implement a GUI/dashboard.
- Schedule the script to run daily (e.g., with `cron`).

---



## Acknowledgments 🌟

- Inspired by price tracking needs for flash sales.
- Uses `BeautifulSoup` for elegant HTML parsing.

---

Happy deal hunting! 🛒🔥  

---
