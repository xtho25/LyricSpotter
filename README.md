# LyricSpotter
A python script that gets the lyrics of the current Spotify song playing.
Inspired by [Overlyrics](https://github.com/CezarGab/Overlyrics).
I recommend using Overlyrics instead of my programm as it has way more functionality. If you are still here then go on and read on how to set up my code below.
# How to set up:

## Download the libraries from requirements.txt using pip:
```
pip install -r requirements.txt
```

## Setting up an app in the Spotify developer portal:
* Go to the [Spotify Developer portal](https://developer.spotify.com/dashboard) and log in to spotify.
* Create an app and set a title and rescription of your choosing. Add as a redirect uri https://google.com/ and make sure you tick the Web API tickbox. Then, click Save.
* 3.Afterwards, got to settings and copy the Client ID and Secret ID and paste them into their respective parameters in the code (line 27 and 28).
* 4.Finally, run the code authorise on the browser that will automatically open, copy the URL that you were redirected to and paste it in the console and press Enter.

# That's it!
If you find any bugs make sure to report them at the Issues tab! And feel free to contribute towards the project! Happy listening!
