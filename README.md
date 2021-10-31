**Price Checker**<br />
A web application to search for input products across several supermarkets' e-commerce to return price, detail of products.
<br /><br />
**Requirements**<br />
Please make sure to install the following packages in order to run this application:<br />
<br />
[*Flask*](https://pypi.org/project/Flask/)<br />
[*pyrebase*](https://pypi.org/project/Pyrebase4/)<br />
[*Wekzeug*](https://pypi.org/project/Werkzeug/)<br />
[*requests*](https://pypi.org/project/requests/)<br />
[*beautifulsoup4*](https://pypi.org/project/beautifulsoup4/)<br />
[*urllib3*](https://pypi.org/project/urllib3/)<br /><br />
[*selenium*](https://pypi.org/project/selenium/)<br /><br />
```pip install -r requirements.txt```<br />
<br />
**Store Modules**<br />
An application will attempt to search input products across 4 main supermarkets' in the UK including [*Sainsburys*](https://www.sainsburys.co.uk/), [*Tesco*](https://tesco.com/), [*Iceland*](https://www.iceland.co.uk/), [*Morrisons*](https://groceries.morrisons.com/).<br />
<br />
**ChromeDriver**<br />
You will need to download corresponding [Chromedriver](https://chromedriver.chromium.org/downloads) to your [chrome version](chrome://version). After installed, you will need to get the path of that ChromeDriver and replace it to the current path inside **offers** folder, **asdaoffers.py**.<br />
<br />
**Authentication API**<br />
Applying the REST API of [pyrebase](https://github.com/thisbejim/Pyrebase) from [Firebase](https://firebase.google.com/) to integrate the authentication to this application.<br />
<br />
**VPN/ IP address**<br />
Ensure you do not use any VPN or proxy as some website get blocked from using proxy such as [*Sainsburys*](https://www.sainsburys.co.uk/) or [*Iceland*](https://www.iceland.co.uk/).<br />
