# ConditionsAlert

Notifications of the following days mountain weather forecasts. 

Email notifications from the Mountain Weather Information Service (MWIS). Designed for busy outdoors people who want to be alerted about the following days weather in mountain regions. 

This programme is designed to be deployed on a small Raspberry Pi using CRON to handle timing of emails. 

## Usage of CRON

Connect to your Raspberry Pi, either headless or with peripherals. 

1. Open terminal
2. Type ```crontab -e```, at this point you will be asked which text editor you prefer. Just select the default option. 
3. Type ```0 9 * * * python /home/pi/ConditionsPy.py```, this will execute the program at 9AM everyday and produce the forecast for tomorrow's weather. If you adjust this be sure to check when MWIS automatically produces tomorrow's forecast as default.

## Usage of SMTP and Gmail

To send an email from a Gmail account you must first adjust the security settings on your account to allow 3rd party applications. It is recommended that you set up a new account for this. For more details click [here](https://support.google.com/accounts/answer/3466521?hl=en)
