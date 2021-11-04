
# Time,Date API 🕛 📅

A simple api that gives you timezone time and dates[for now]


## API Reference

### API EndPoint

```http
https://time-date-api.sas2k.repl.co/
```

#### Get TimeZone

```http
  GET /time/get/{timezone}
```

| code      |    country    | city                       |
| :-------- | :-------      | :------------------------- |
| `sl`      |  Sri Lanka    |   Colombo                  |
| `eusa`    |  Eastern USA  |   Eastern US Time          |
| `aus`     |  Australia    |   Brisbane                 |
| `lon`     |  England      |   London                   |


## Usage/Examples

```python
import requests

resoponse = requests.get('https://time-date-api.sas2k.repl.co/time/get/sl')

print(resoponse.text)
```


## Badges

[![Run on Repl.it](https://repl.it/badge/github/Sas2k/Time-Date-API)](https://repl.it/github/Sas2k/Time-Date-API)


## Authors

- [@Sas2k](https://www.github.com/Sas2k)

