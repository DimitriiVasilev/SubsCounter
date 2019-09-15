# Description
This project is created to collect information about communities in Russian social media 
VKontakte (VK). Currently it looks how many subscribers communities have and puts these 
numbers into database. For gathering data this project uses official VK API. This gives 
more precise information than just parse web page as an anonymous user. SQLite is utilized 
for saving information. Also, it's decided to use standard `sqlite3` lib for working with 
database because it would be too much to utilize more sophisticated libs, like `SQLAlchemy`, just
for saving number of community subscribers.

## Requirements
To run this app you need to provide your VK access token. It is needed for VK API in order 
to be authorized when community data is collected. The easiest way to get the token is to go to 
https://vk.com/apps?act=manage, press `Create app` button and follow further instructions.
Next, visit app's settings and copy `Service token`. That's it.  
Also, you have to install `requests` package. To do this just run:
        
        pip3 install -r requrements.txt

## Settings
Settings of this project are in `settings.json`. There you can provide your access token that
was got in previous paragraph and communities you want to collect information about.  
To provide your token replace `PUT YOUR TOKEN HERE` string on it. To add more communities
append their names and ids to `communities` section. There are several ways to find out the community 
id. For example, you can use http://regvk.com/id/. Do not forget than trailing comma is invalid
in json format.  
In the end your settings file will look kind of like this:
```json
{
  "access_token": "12345abcde",
  "communities": {
    "rambler/news": 97751087,
    "rambler/mail": 36023798,
    "rambler/horoscopes": 86125491,
    "championat": 1331201,
    "championat.auto": 147610669,
    "championat.cybersport": 77903189,
    "livejournal": 25072924,
    "afisha": 1672730
  }
}
```