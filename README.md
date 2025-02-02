<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>093697984c0349aaa496c4215607eb61</title>
  <style>
    html {
      line-height: 1.5;
      font-family: Georgia, serif;
      font-size: 20px;
      color: #1a1a1a;
      background-color: #fdfdfd;
    }
    body {
      margin: 0 auto;
      max-width: 36em;
      padding-left: 50px;
      padding-right: 50px;
      padding-top: 50px;
      padding-bottom: 50px;
      hyphens: auto;
      overflow-wrap: break-word;
      text-rendering: optimizeLegibility;
      font-kerning: normal;
    }
    @media (max-width: 600px) {
      body {
        font-size: 0.9em;
        padding: 1em;
      }
      h1 {
        font-size: 1.8em;
      }
    }
    @media print {
      body {
        background-color: transparent;
        color: black;
        font-size: 12pt;
      }
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      h2, h3, h4 {
        page-break-after: avoid;
      }
    }
    p {
      margin: 1em 0;
    }
    a {
      color: #1a1a1a;
    }
    a:visited {
      color: #1a1a1a;
    }
    img {
      max-width: 100%;
    }
    h1, h2, h3, h4, h5, h6 {
      margin-top: 1.4em;
    }
    h5, h6 {
      font-size: 1em;
      font-style: italic;
    }
    h6 {
      font-weight: normal;
    }
    ol, ul {
      padding-left: 1.7em;
      margin-top: 1em;
    }
    li > ol, li > ul {
      margin-top: 0;
    }
    blockquote {
      margin: 1em 0 1em 1.7em;
      padding-left: 1em;
      border-left: 2px solid #e6e6e6;
      color: #606060;
    }
    code {
      font-family: Menlo, Monaco, 'Lucida Console', Consolas, monospace;
      font-size: 85%;
      margin: 0;
    }
    pre {
      margin: 1em 0;
      overflow: auto;
    }
    pre code {
      padding: 0;
      overflow: visible;
      overflow-wrap: normal;
    }
    .sourceCode {
     background-color: transparent;
     overflow: visible;
    }
    hr {
      background-color: #1a1a1a;
      border: none;
      height: 1px;
      margin: 1em 0;
    }
    table {
      margin: 1em 0;
      border-collapse: collapse;
      width: 100%;
      overflow-x: auto;
      display: block;
      font-variant-numeric: lining-nums tabular-nums;
    }
    table caption {
      margin-bottom: 0.75em;
    }
    tbody {
      margin-top: 0.5em;
      border-top: 1px solid #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
    }
    th {
      border-top: 1px solid #1a1a1a;
      padding: 0.25em 0.5em 0.25em 0.5em;
    }
    td {
      padding: 0.125em 0.5em 0.25em 0.5em;
    }
    header {
      margin-bottom: 4em;
      text-align: center;
    }
    #TOC li {
      list-style: none;
    }
    #TOC ul {
      padding-left: 1.3em;
    }
    #TOC > ul {
      padding-left: 0;
    }
    #TOC a:not(:hover) {
      text-decoration: none;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    div.columns{display: flex; gap: min(4vw, 1.5em);}
    div.column{flex: auto; overflow-x: auto;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
    ul.task-list li input[type="checkbox"] {
      width: 0.8em;
      margin: 0 0.8em 0.2em -1.6em;
      vertical-align: middle;
    }
    .display.math{display: block; text-align: center; margin: 0.5rem auto;}
  </style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<p>🏋️ FitLog: Automated Workout Tracker</p>
<p>📌 Overview</p>
<p>FitLog is a Python-based project that automates workout tracking
using the Nutritionix API for exercise analysis and Google Sheets API
for logging workouts. Simply input your workout, and the script will log
the details like calories burned, duration, and timestamp in a Google
Sheet.</p>
<p>🚀 Features</p>
<p>✅ Fetch exercise details using Nutritionix API</p>
<p>✅ Automatically logs workouts with date &amp; time</p>
<p>✅ Google Sheets Integration for seamless tracking</p>
<p>✅ Real-time UTC to IST conversion</p>
<p>✅ User-friendly input system</p>
<p>🛠️ Technologies Used</p>
<p>Python 🐍</p>
<p>Nutritionix API 🍏</p>
<p>Google Sheets API 📊</p>
<p>Requests Library 🌐</p>
<p>DateTime &amp; Pytz ⏳</p>
<p>📜 Prerequisites</p>
<p>Before running the script, make sure you have:</p>
<p>Python installed (&gt;=3.6)</p>
<p>Nutritionix API credentials (APP_ID &amp; API_KEY)</p>
<p>A Google Sheets API endpoint</p>
<p>Required libraries installed:</p>
<p>pip install requests pytz</p>
<p>🔧 Setup Instructions</p>
<p>Clone this repository:</p>
<p>git clone https://github.com/yourusername/FitLog.git cd FitLog</p>
<p>Replace your_app_id, your_api_key, and your_google_sheet_api_endpoint
in the script.</p>
<p>Run the script:</p>
<p>python workout_tracker.py</p>
<p>Input your exercise details when prompted.</p>
<p>Check your Google Sheet for updated records!</p>
<p>📌 Code Snippet</p>
<p>import requests from datetime import datetime import pytz</p>
<p>APP_ID = “your_app_id” API_KEY = “your_api_key” EXERCISE_ENDPOINT =
“https://trackapi.nutritionix.com/v2/natural/exercise” SHEET_ENDPOINT =
“your_google_sheet_api_endpoint”</p>
<p>exercise_text = input(“Tell me which exercise you did:”)</p>
<p>headers = { “x-app-id”: APP_ID, “x-app-key”: API_KEY, “Content-Type”:
“application/json” }</p>
<p>response = requests.post(url=EXERCISE_ENDPOINT, json={“query”:
exercise_text}, headers=headers) result = response.json()</p>
<h1 id="convert-utc-time-to-ist">Convert UTC time to IST</h1>
<p>utc_now = datetime.utcnow() ist_now =
utc_now.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(“Asia/Kolkata”))</p>
<p>India_date = ist_now.strftime(“%d/%m/%Y”) India_time =
ist_now.strftime(“%X”)</p>
<p>for exercise in result[“exercises”]: sheet_inputs = { “workout”: {
“date”: India_date, “time”: India_time, “exercise”:
exercise[“name”].title(), “duration”: exercise[“duration_min”],
“calories”: exercise[“nf_calories”] } }</p>
<pre><code>sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers={&quot;Content-Type&quot;: &quot;application/json&quot;})
print(sheet_response.text)</code></pre>
<p>🔥 Future Enhancements</p>
<p>📊 Add a dashboard for visual workout insights</p>
<p>📱 Create a mobile-friendly UI</p>
<p>🔄 Automate daily reminders for workout logging</p>
<p>📞 Contact</p>
<p>For any queries, feel free to reach out:</p>
<p>Email: <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="0d7462787f2368606c64614d68756c607d6168236e6260">[email&#160;protected]</a></p>
<p>GitHub: yourusername</p>
<p>💪 Stay fit, stay strong! #Python #Automation #FitnessTracker
#WorkoutLog</p>
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body>
</html>
