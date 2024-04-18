from fake_useragent import UserAgent
from requests import get
from re import findall

ua = UserAgent()

def get_proxies(url):
    text = ""
    response = get(url, headers={'User-Agent': ua.random})
    content = response.text.replace("<span> : </span> <em>", ":")
    content = content.replace("</td><td>", ":")
    for proxy, port in findall('((?:\d{1,3}\.){3}\d{1,3}):(\d+)', content):
        text += proxy + ":" + port + "\n"
    print("+", len(text.splitlines()))
    return text

proxies = [
    get_proxies('https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all'),
    get_proxies('https://proxysource.org/api/proxies/getWorkingProxies?apiToken=17580e4438910c287cef15dca10b7912a26&latencyMax=15000&latencyMin=0&outputMode=plaintext&uptimeMax=100&uptimeMin=30'),
    "\n".join(
    get_proxies(
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
    ).splitlines()[2:]),
    get_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt'),
    "\n".join(
    get_proxies(
        "https://www.freeproxychecker.com/result/socks4_proxies.txt"
    ).splitlines()[7:]),
    get_proxies('https://multiproxy.org/txt_all/proxy.txt'),
    get_proxies('http://rootjazz.com/proxies/proxies.txt'),
    get_proxies('http://ab57.ru/downloads/proxyold.txt'),
    get_proxies('https://www.proxy-list.download/api/v1/get?type=socks4'),
    get_proxies('https://www.proxyscan.io/download?type=socks4'),
    get_proxies('http://proxydb.net/?protocol=socks4'),
    get_proxies('https://api.openproxylist.xyz/socks4.txt'),
    get_proxies('https://api.openproxylist.xyz/socks5.txt'),
    get_proxies('https://api.openproxylist.xyz/http.txt'),
    get_proxies('https://proxyspace.pro/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt'),
    get_proxies('http://worm.rip/socks4.txt'),
    get_proxies('https://www.proxy-list.download/api/v1/get?type=socks4'),
    get_proxies('https://www.proxyscan.io/download?type=socks4'),
    get_proxies('https://www.my-proxy.com/free-socks-4-proxy.html'),
    get_proxies('http://www.socks24.org/feeds/posts/default'),
    get_proxies('https://www.freeproxychecker.com/result/socks4_proxies.txt'),
    get_proxies('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt'),
    get_proxies('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS4.txt'),
    get_proxies('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/SOCKS5.txt'),
    get_proxies('https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt'),
    get_proxies('https://api.openproxylist.xyz/socks5.txt'),
    get_proxies('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5'),
    get_proxies('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5'),
    get_proxies('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5'),
    get_proxies('https://kabak.top/socks4'),
    get_proxies('https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&simplified=true'),
    get_proxies('https://proxyspace.pro/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt'),
    get_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt'),
    get_proxies('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt'),
    get_proxies('https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/socks.txt'),
    get_proxies('http://worm.rip/socks5.txt'),
    get_proxies('http://www.socks24.org/feeds/posts/default'),
    get_proxies('https://www.freeproxychecker.com/result/socks5_proxies.txt'),
    get_proxies('https://www.proxy-list.download/api/v1/get?type=socks5'),
    get_proxies('https://www.proxyscan.io/download?type=socks5'),
    get_proxies('https://www.my-proxy.com/free-socks-5-proxy.html'),
    get_proxies('https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt'),
    get_proxies('https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt'),
    get_proxies('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt'),
    get_proxies('https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt'),
    get_proxies('https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt'),
    get_proxies('https://api.proxyscrape.com/?request=displayproxies&proxytype=http'),
    get_proxies('https://api.openproxylist.xyz/http.txt'),
    get_proxies('http://alexa.lr2b.com/proxylist.txt'),
    get_proxies('https://multiproxy.org/txt_all/proxy.txt'),
    get_proxies('https://proxyspace.pro/http.txt'),
    get_proxies('https://proxyspace.pro/https.txt'),
    get_proxies('https://proxy-spider.com/api/proxies.example.txt'),
    get_proxies('http://proxysearcher.sourceforge.net/Proxy%20List.php?type=http'),
    get_proxies('https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'),
    get_proxies('https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt'),
    get_proxies('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt'),
    get_proxies('https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt'),
    get_proxies('https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt'),
    get_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt'),
    get_proxies('https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt'),
    get_proxies('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt'),
    get_proxies('https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt'),
    get_proxies('https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt'),
    get_proxies('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt'),
    get_proxies('https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt'),
    get_proxies('https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/https.txt'),
    get_proxies('https://raw.githubusercontent.com/BlackSnowDot/proxylist-update-every-minute/main/http.txt'),
    get_proxies('https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt'),
    get_proxies('https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt'),
    get_proxies('http://rootjazz.com/proxies/proxies.txt'),
    get_proxies('http://spys.me/proxy.txt'),
    get_proxies('https://sheesh.rip/http.txt'),
    get_proxies('http://worm.rip/http.txt'),
    get_proxies('http://www.proxyserverlist24.top/feeds/posts/default'),
    get_proxies('https://www.proxy-list.download/api/v1/get?type=htt'),
    get_proxies('https://www.proxyscan.io/download?type=http'),
    get_proxies('https://www.my-proxy.com/free-anonymous-proxy.html'),
    get_proxies('https://www.my-proxy.com/free-transparent-proxy.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-2.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-3.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-4.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-5.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-6.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-7.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-8.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-9.html'),
    get_proxies('https://www.my-proxy.com/free-proxy-list-10.html'),
    get_proxies('https://www.freeproxychecker.com/result/http_proxies.txt'),
    get_proxies('https://hidemy.name/en/proxy-list/?type=4#list'),
    get_proxies('https://www.socks-proxy.net/'),
    get_proxies('https://www.my-proxy.com/free-socks-4-proxy.html')
    ]

open("output.txt", "w").write('\n'.join(proxies))
