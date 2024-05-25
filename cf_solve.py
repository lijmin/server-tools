import requests


def main():
    solveUrl = "http://118.193.37.214:9092/v1/solve"
    
    sitekey = "0x4AAAAAAAI8vI5UdenWQwF3"
    url = "https://blackvid.space/embed?tmdb=1673&season=1episode=2"
    query_data = { "sitekey": sitekey, "url": url }
    response = requests.get(solveUrl, json=query_data)
    res = response.text
    print(res)


if __name__ == '__main__':
    main()

    

