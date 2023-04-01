# Typing tests bot
A typing bot for different typing test websites.
<br>
He writes at more than 400 words per minute !

[Capture vidéo du 2023-04-01 14-09-16.webm](https://user-images.githubusercontent.com/96385330/229289271-99cd5867-789e-412a-bbfd-22e8496ed651.webm)

## Avalaible typing tests :
- [10fastfingers](https://10fastfingers.com)

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
            "get-with": "id or class",
            "value": "The id or the class of the buton"
        }
        
    ],
    "word-input": //The input or the bot must write the words
    {
        "get-with": "id or class",
        "value": "The id or the class of the input"
    },
    "word-to-write": //The word that the bot should write
    {
        "get-with": "id or class", 
        "value": "The id or the class of the input"
    }
}
```
- You add the website name to `AVALAIBLE_WEBSITES` in `main.py`.
- You add the website to the Avalaible typing tests section of the `Readme.md` file
