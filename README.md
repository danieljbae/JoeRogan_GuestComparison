# Podcast_GuestComparison

## About the Project
Using the YouTube API, this repo visualizes how different guests on Joe Rogan's podcasr fare against another (animated across time). 

The basis for the comparisons are drawn from simple community enagagement stats such as: view count, like count, dislike count, comment count


Some metrics I considered were:
* guest contraversy with bubble color
* community engagement with bubble size  

Below is a snippet of the plot:

![alt text](https://github.com/danieljbae/Podcast_GuestComparison/blob/main/demo_ss.PNG)


## Getting Started 

### Prerequisites
Start Google project to generate API Key and choose YouTube API service @ https://console.developers.google.com/

#### Windows
Install virtualenv to manage packages and create enviroment
```sh
pip install virtualenv
virtualenv <your-env>
```
Activate your enviroment
```sh
<your-env>\Scripts\activate
```
Install packages:
* google-api-python-client
```sh
<your-env>\Scripts\pip.exe install google-api-python-client
```
* plotly
* regex
* pandas
```sh
<your-env>\Scripts\pip.exe install plotly
<your-env>\Scripts\pip.exe install regex
<your-env>\Scripts\pip.exe install pandas
```
#### Mac/Linux
Install virtualenv to manage packages and create enviroment
```sh
pip install virtualenv
virtualenv <your-env>
```
Activate your enviroment
```sh
source <your-env>/bin/activate
```
Install packages:
* google-api-python-client
```sh
<your-env>/bin/pip install google-api-python-client
```
* plotly
* regex
* pandas
```sh
<your-env>/bin/pip install plotly
<your-env>/bin/pip install regex
<your-env>/bin/pip install pandas
```
### Sources and references:
* getting started with Google APIs: https://github.com/googleapis/google-api-python-client
* YouTube API v3 Documentation: https://developers.google.com/youtube/v3/docs?hl=en
