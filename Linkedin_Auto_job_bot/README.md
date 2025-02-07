---

# LinkedIn Job Application Bot 🤖

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Selenium](https://img.shields.io/badge/Automation-Selenium-green)  
![LinkedIn](https://img.shields.io/badge/Platform-LinkedIn-blue)

Automate LinkedIn job applications with this Python script using Selenium. Apply to multiple "Easy Apply" jobs with predefined filters in seconds!

---

## Features ✨

- **Auto-Login**: Securely logs into LinkedIn using your credentials.
- **Job Search Filters**: Targets jobs with predefined filters (e.g., Python Developer roles in India).
- **Easy Apply Automation**: Fills out and submits "Easy Apply" forms.
- **Resume Handling**: Uploads pre-saved resumes from your LinkedIn profile.
- **Phone Number Input**: Automatically populates phone number fields.
- **Multi-Job Support**: *(Work in Progress)* Loop to apply to multiple jobs (code commented out for testing).

---

## Installation 📦

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/linkedin-job-bot.git
   cd linkedin-job-bot
   ```

2. **Install Dependencies**:
   ```bash
   pip install selenium
   ```

3. **Set Up ChromeDriver**:
   - Download [ChromeDriver](https://sites.google.com/chromium.org/driver/) matching your Chrome version.
   - Add the ChromeDriver executable to your system PATH or update the script to point to its location.

4. **Configure Credentials**:
   - Create a `details.py` file with:
     ```python
     EMAIL_ID = "your_linkedin_email@example.com"
     PASSWORD = "your_linkedin_password"
     PHONE_NO = "your_phone_number"  # e.g., "9876543210"
     ```

---

## Usage 🖥️

1. **Customize the Job Search URL**:
   - Replace the `Linkedin_URL.get(...)` line with your LinkedIn job search URL (with desired filters and "Easy Apply" enabled).

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Watch the Magic**:
   - The bot will log in, navigate to jobs, and apply to the first "Easy Apply" listing.
   - *(Uncomment the loop section to apply to multiple jobs.)*

---

## Configuration 🔧

| Variable       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| `EMAIL_ID`     | Your LinkedIn email (set in `details.py`).                                 |
| `PASSWORD`     | Your LinkedIn password (set in `details.py`).                              |
| `PHONE_NO`     | Your phone number for application forms (set in `details.py`).             |
| `Linkedin_URL` | Customize the job search URL in the script (e.g., location, job title).    |

---

## Notes ⚠️

1. **LinkedIn Restrictions**:
   - LinkedIn may block automated scripts if used aggressively. Use responsibly!
   - Avoid running the script too frequently to prevent account restrictions.

2. **Dynamic Selectors**:
   - LinkedIn’s UI changes frequently. Update XPATH/CSS selectors if the script breaks.

3. **Resume Requirement**:
   - Ensure your resume is pre-uploaded to LinkedIn under *"Job Application Settings"*.

4. **Multi-Job Application**:
   - The looped multi-application feature is commented out. Test carefully before enabling.

---

## Screenshot 🖼️

![image](https://github.com/user-attachments/assets/30addd47-78f6-45ec-92e8-9816b9b91824)
![image](https://github.com/user-attachments/assets/39b475d0-0b83-4790-9197-57b70b337ba7)
![image](https://github.com/user-attachments/assets/1e6325b2-243a-4b07-b13f-5ac808eb1aa9)


*Example of the bot applying to a job.*

---

## Ethical Use Disclaimer ❗

This project is for **educational purposes only**. Always:
- Follow LinkedIn’s [User Agreement](https://www.linkedin.com/legal/user-agreement).
- Respect job posters’ time and avoid spamming.
- Use automation judiciously.

---



## Contributions 🤝

Feel free to:
- Improve error handling for UI changes.
- Add support for CAPTCHA bypass (if ethical).
- Enhance multi-job application logic.

---

Happy job hunting! 🚀  
