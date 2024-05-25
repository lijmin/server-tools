import requests


def main():
    url = "http://118.193.37.214:9092/v1/unpack"
    data = "eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\\\b'+e(c)+'\\\\b','g'),k[c])}}return p}('1.t=\"//a-2.5.6/7/8.9\";1.b=\" \";1.c=\"//a-2.5.6/v/3.4?s=d&e=f&g=h\";1.i=\"3.4\";1.u=\"a-2\";1.x=\"\";1.w=0;1.l=\"\";1.r=\"q%p%o%n.m%k%j\";',34,34,'|MDCore|delivery34|ba176f42f3f5f624d3991820711e628e|mp4|mxcontent|net|thumbs|4nw7koe4uv1kv0|jpg||furl|wurl|zzMEqkq9_CBmj7Zu03QkfQ||1714120867|_t|1714104452|vfile|2F4nw7koe4uv1kv0|2Fe|adTagUrl|ag|2Fmixdrop|2F|3A|https|referrer||poster|vserver||chromeInject|remotesub'.split('|'),0,{}))"
    
    query_data = { "data": data }
    response = requests.get(url, json=query_data)
    res = response.text
    print(res)


if __name__ == '__main__':
    main()

    

