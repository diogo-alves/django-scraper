import scrapy


class ProxiesSpider(scrapy.Spider):
    name = 'proxies'
    start_urls = [
        'https://hidemy.name/en/proxy-list/',
    ]

    def parse(self, response):
        table_rows = response.css('.table_block table tbody tr')
        for row in table_rows:
            yield self.parse_proxy(row)
        next_page = response.css(
            'div.pagination .next_array a::attr(href)'
        ).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_proxy(self, row):
        return {
            'ip_address': row.css('td::text')[0].get(),
            'port': row.css('td::text')[1].get(),
            'country': row.css('td .country::text').get(),
            'city': row.css('td .city::text').get(),
            'speed': row.xpath('//td//p/text()')[3].re_first(r'\d{1,}'),
            'protocol': row.css('td::text')[4].get(),
            'anonymity': row.css('td::text')[5].get(),
        }
