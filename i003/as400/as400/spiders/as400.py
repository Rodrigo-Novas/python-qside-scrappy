import scrapy
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from scrapy.http import FormRequest
from .. loger import logard
class as400Spider(scrapy.Spider):
    name = 'as400'
    allowed_domains = ['i0003.srv.skf.net']
    login_url = ['http://i0003.srv.skf.net:2004/ibm/console/logon.jsp']
    start_urls = ['http://i0003.srv.skf.net:2004/ibm/console/login.do?action=secure']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    #loguin

    def parse(self, response):
        print(str(response.body))
        logard.info(str(response.body))
        headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "es-419,es;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Cookie": "NAVIGATORSID=0000fgit76ygsNC6zyvXUIs3z2f:743e7fce-b9ec-4549-bb6a-633c8bc3b3af; WASReqURL=http://:2004/ibm/console/login.do?action=secure",
        "Host": "i0003.srv.skf.net:2004",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

        return FormRequest.from_response(response,
            url='http://i0003.srv.skf.net:2004/ibm/console/logon.jsp',
            formname='logonForm',
            formdata={'j_username': 'UB68563',  # login instead of username
                                'j_password': 'UB68563'},
            clickdata = {
            'type': 'submit',
            'class': 'tiv_btn' 
            },
            callback=self.started,
            headers= headers,
            method="POST")

    def started(self, response):
        # Reload the landing page
        print("log")
        print(str(response.body))
        return Request(url=self.start_urls[0], callback=self.logged_in)

    def logged_in(self, response):
        print("dentro")
        # logged in page here
        print("-------------------------", "-----------", "\n", sep="*", end="Login")
        print(str(response.body))
#     def parse(self, response):
#     ##This function is called before crawling starts
#         return Request(url=self.start_urls[0], callback="login")

#     def login(self, response):
#     ##Generates a login request
#         return FormRequest.from_response(
#             response, 
#             formdata = {
#             'j_username': 'UB68563', 
#             'j_password': 'UB68563'
#             }, 
#             clickdata = {
#             'type': 'submit', 
#             'class': 'tiv_btn', 
#             'value': 'Iniciar sesión'
#             }, 
#             callback = self.check_login_response
#         )

#     def check_login_response(self, response):
#     ##Check the response returned by a login request to see if we are successfully logged in.
#         print("-------------------------", "-----------", "\n", sep="*", end="Login")
#         print(str(response.body))