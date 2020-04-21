# ImgCrawler
ImgCrawler is a useful image crawler that I used to download pretty pictures. A simple command, download thousands of beautiful pictures.  
# 1. Version
1.0.0
- 1.0.0  
    > Enable netbian, it is just a runnable instance, I have no time to design a robust project right now. 
    
    
# 1. Picture Sources
- [x] [netbian](http://pic.netbian.com/)
- [ ] [uhdpixel](https://uhdpixel.com/)

# 2. Useage

## 2.1 Precondition
- [x] python 3.5+
- [x] pip or conda(recommend)

## 2.2 Run
- netbian  
    You are able to download one kind of pretty pictures from netbian by running
    ```text
    python manage.py netbian <category>  # e.g. python manage.py netbian dongman
    ```
    also, you could do not specify category to download all. 
    ```text
    python manage.py netbian
    ```
