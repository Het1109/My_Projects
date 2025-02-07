
---

# ☔ Rain Alert WhatsApp Bot  

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![OpenWeatherMap](https://img.shields.io/badge/API-OpenWeatherMap-orange)  
![Twilio](https://img.shields.io/badge/SMS-Twilio-green)  

Get automated WhatsApp alerts when rain is predicted in your area! Built with Python, OpenWeatherMap API, and Twilio.  

---

## Features ✨  
- **12-Hour Forecast**: Checks weather data for the next 12 hours (4 intervals of 3 hours).  
- **Rain Detection**: Alerts you if any precipitation (rain, snow, etc.) is detected.  
- **WhatsApp Integration**: Sends alerts directly to your WhatsApp via Twilio.  
- **Geolocation Support**: Configured for Jakarta by default (easily customizable to any location).  

---

## Installation 📦  

1. **Clone the Repository**:  
   ```bash  
   git clone https://github.com/your-username/rain-alert-bot.git  
   cd rain-alert-bot  
   ```  

2. **Install Dependencies**:  
   ```bash  
   pip install requests twilio  
   ```  

3. **Get API Keys**:  
   - Sign up for [OpenWeatherMap](https://openweathermap.org/api) (free tier).  
   - Sign up for [Twilio](https://www.twilio.com/) (free trial credits available).  

4. **Configure Credentials**:  
   Replace placeholder values in the script:  
   ```python  
   api_key = "YOUR_OPENWEATHERMAP_API_KEY"  
   account_sid = "YOUR_TWILIO_ACCOUNT_SID"  
   auth_token = "YOUR_TWILIO_AUTH_TOKEN"  
   to="whatsapp:+YOUR_PHONE_NUMBER"  # e.g., "+919876543210"  
   ```  

---

## Usage 🚀  

1. **Customize Location** (Optional):  
   Modify the `weather_params` in the script:  
   ```python  
   weather_params = {  
       "lat": YOUR_LATITUDE,  
       "lon": YOUR_LONGITUDE,  
       "appid": api_key,  
       "cnt": 4,  # 12-hour forecast  
   }  
   ```  

2. **Run the Script**:  
   ```bash  
   python main.py  
   ```  

3. **Receive Alerts**:  
   If rain is predicted, you'll get a WhatsApp message like:  
   > *"Umbrella le lena bhai Baarish ho rahi heh.☔🌧️"*  

---

## Example Output 📱  
![Screenshot from 2025-02-07 18-02-52](https://github.com/user-attachments/assets/0ad87282-6a19-4c35-84ff-0317dab9cee1)
![image](https://github.com/user-attachments/assets/6589e4d6-1c1c-4154-af55-682791a9d048)


---

## Dependencies 📚  
- `requests` - For API calls to OpenWeatherMap.  
- `twilio` - For sending WhatsApp messages.  

---

## Notes ⚠️  
- **API Limits**: OpenWeatherMap free tier allows 1000 calls/day.  
- **Security**: Never commit API keys/Twilio tokens to GitHub. Use environment variables for production.  
- **Global Use**: Works for any location worldwide (update latitude/longitude).  

---

Stay dry and code on! 🌧️💻  

---
