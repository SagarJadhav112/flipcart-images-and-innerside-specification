import scrapy


class FlipcartSpider(scrapy.Spider):
    name = 'flipcartimages'
    #allowed_domains = ['flipcart.com']
    # start_urls = ["https://www.flipkart.com/search?q=phone"]

    def start_requests(self):
        yield scrapy.Request (
            url="https://www.flipkart.com/search?q=phone&page=",
            callback=self.parse)

    def parse(self,response):
        link1 = response.xpath("//div[@class='_2kHMtA']/child::a/@href")
        link2=f"https://www.flipkart.com{link1}"
        
        for i in link1:
            a=f"https://www.flipkart.com{i.get()}"
            yield scrapy.Request (
            url=a,
            callback=self.innerlink)
            
        next_page = response.xpath("//span[text()='Next']/parent::a/@href").get()
        if next_page :
            next_page_url = f"https://www.flipkart.com{next_page}"
            yield scrapy.Request(next_page_url,callback=self.parse)
            
    def innerlink(self,response):

        name = response.xpath(".//div[@class='aMaAEs']/child::div/child::h1//text()").get()
        price = response.xpath("//div[@class='_25b18c'][1]/child::div[@class='_30jeq3 _16Jk6d']/text()").get().replace('₹','')
        in_the_box = response.xpath(".//td[text()='In The Box']/following::li[1]/text()").get()
        model_number = response.xpath(".//td[text()='Model Number']/following::li[1]/text()").get()
        model_name = response.xpath(".//td[text()='Model Name']/following::li[1]/text()").get()
        color = response.xpath(".//td[text()='Color']/following::li[1]/text()").get()
        browse_type = response.xpath(".//td[text()='Browse Type']/following::li[1]/text()").get()
        sim_type = response.xpath(".//td[text()='SIM Type']/following::li[1]/text()").get()
        hybrid_sim_slot = response.xpath(".//td[text()='Hybrid Sim Slot']/following::li[1]/text()").get()
        touchscreen = response.xpath(".//td[text()='Touchscreen']/following::li[1]/text()").get()
        otg = response.xpath(".//td[text()='OTG Compatible']/following::li[1]/text()").get()
        fast_charging = response.xpath(".//td[text()='Quick Charging']/following::li[1]/text()").get()
        SAR_value = response.xpath(".//td[text()='SAR Value']/following::li[1]/text()").get()
        images= response.xpath(".//div[@class='_2E1FGS']/child::img/@src").getall()
        
        yield{
            "name" :name,
            "price" : price,
            "in_the_box" : in_the_box,
            "model_number":model_number,
            "model_name" : model_name,
            "color":color,
            "browse_type":browse_type,
            "sim_type":sim_type,
            "hybrid_sim_slot":hybrid_sim_slot,
            "touchscreen":touchscreen,
            "otg":otg,
            "fast_charging":fast_charging,
            "SAR_value":SAR_value,
            "images":images
            
            
          }  

        



       
            
        







           

        
        

   
    


        
            
                

            
        
        