# Podcast_GuestComparison
Using the YouTube API, this repo visualizes how different guests fare against another (animated across time). 


## About the Project
Using the YouTube API, this repo visualizes how different guests for on Joe Rogan's podcast fare against another throughout time. 

The basis for the comparisons are drawn from simple community enagagement stats such as: view count, like count, dislike count, comment count

Some interesting metrics I considered was:
* guest contraversy with bubble color
* community engagement with bubble size  


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






### Sources:
* https://github.com/googleapis/google-api-python-client
* 
