# How make a template file

## Structure

A template is a liste of application.

You can make two type of application:
- Normal app
- Browser app

A normal app is an application that just open itself.

A browser app is an application that open a browser with a list of urls.

```json
{
    "Name_of_the_template": [
        {
            //This is a normal app
            "path": "path/to/exe"
        },
        { //This is a browser app
            "path": "path/to/browser/exe",
            "urls": [ // You can specfiy multiple urls to open
                "url1",
                "url2"
            ]
        }
    ]
}
```


## Example

For example, if you want to make a template that open chrome with youtube, you can do this:

```json
{
    "Youtube": [
        {
            "path": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            "urls": [
                "https://www.youtube.com"
            ]
        }
    ]
}
```

Or if you want to make a template that VSCode and firefox with github and google:

```json
{
    "Programing": [
        {
            "path": "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        },
        {
            "path": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
            "urls": [
                "https://github.com",
                "https://google.com"
            ]
        }
    ]
}
```