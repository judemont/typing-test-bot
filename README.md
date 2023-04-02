# Typing tests bot
A typing bot for different typing test websites.
<br>
He writes at more than 400 words per minute !

[Capture vidéo du 2023-04-01 14-09-16.webm](https://user-images.githubusercontent.com/96385330/229289271-99cd5867-789e-412a-bbfd-22e8496ed651.webm)

## Avalaible typing tests :
- [10fastfingers](https://10fastfingers.com)
- [typing.com](https://typing.com)
- [speedtypingonline](https://speedtypingonline.com)
- [keyhero](https://keyhero.com)

## Usage :
 If you are running linux replace `python3` with `python`.

Download and install selenium :
```bash
sudo apt install python-selenium
```
```bash
python main.py [name of the typing test]
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
- You complete the file like that : 

```jsonc
{
    "url": "The complete url of the test",
    "buttons-to-click": //All the butons to click to start the test
    [
        {
            "xpath": "The xpath of the button or the element." 
        }
        
    ],
    "input": //The input or the bot must write the words or the letter. If there is no input you can use 'body' for value.
    {
        "css-selector": "The xpath of the input.'" 
    },
    "to-write": //The word that the bot should write
    {
        "css-selector": "The xpath of the element.'" 
    }, 
    "next-key": "The next key to press after each words or letters. Example: ' ' or '\n'"

}
```
- You add the website name to `AVAILABLES_WEBSITES` in `main.py`.
- You add the website to the Avalaible typing tests section of the `Readme.md` file
