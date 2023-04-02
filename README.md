# Typing tests bot
A typing bot for different typing test websites.
<br>
He writes at more than 400 words per minute !

[Capture vidéo du 2023-04-01 14-09-16.webm](https://user-images.githubusercontent.com/96385330/229289271-99cd5867-789e-412a-bbfd-22e8496ed651.webm)

## Avalaible typing tests :
- [10fastfingers](https://10fastfingers.com)
- [typing.com](https://typing.com)

## Usage :
 If you are running linux replace `python3` with `python`.

Download and install selenium :
```bash
sudo apt install python-selenium
```
```bash
python main.py [website]
```
`--help or -h to print the help`
### Example :
```bash
python main.py 10fastfingers
```
## Contribute :
<b>The contributions are very appreciated</b>
### Add typing test website :
To add typing test website you :
- Creat a new json file in the `typing-test-websites` folder. 
- (The file name must be the name of the test.)
- You complete the file with like that : 

```jsonc
{
    "url": "The complete url of the test",
    "buttons-to-click": //All the butons to click to start the test
    [
        {
            "css-selector": "The css selector of the button. Example: '#acoolid'" 
        }
        
    ],
    "input": //The input or the bot must write the words or the letter. If there is no input you can use 'body' for value.
    {
        "css-selector": "The css selector of the input. Example: '.acoolclass'" 
    },
    "word-to-write": //The word that the bot should write
    {
        "css-selector": "The css selector of the element. Example: '.acoolclass'" 
    }, 
    "next-key": "The next key to press after each words or letters. Example: ' ' or '\n'"

}
```
- You add the website name to `AVALAIBLE_WEBSITES` in `main.py`.
- You add the website to the Avalaible typing tests section of the `Readme.md` file
