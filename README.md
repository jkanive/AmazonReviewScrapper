# Amazon Review Scrapper

##Introduction
This is a simple spider written using the beautiful [Scrapy](https://scrapy.org/) a Python framework for website scrapping.

## How to Run the program
As mentioned above this run on Scrapy framework so make sure you have scrapy installed on your machine. Before that you should have
Python 2.7 and above on your machine.

**Note** These instructions are written for Mac. You will have to search for similar command for Windows and Linux

### Setup
```
$ brew install python
```

```
$ pip install Scrapy
```

If you run into error while installing please resolve it by checking Google or Stackoverflow. (I had to do this when testing it on *Early 2008 Mac*)

### Execution
1. Now run the below command and see if you are able to see the amazon_review spider listed after the command as below.

  ```
  $ scrapy list
  amazon_review
  ```

2. Populate the amazonreviewpages.txt with all the pages of the reviews. To do this I have a simple python script you can run as below.

  ```
  $ python generateInputLinks.py https://www.amazon.com/Muse-Brain-Sensing-Headband-Black/dp/B00LOQR37C 33
  ```

  ```
  $ python generateInputLinks.py https://www.amazon.com/<Product Name>/dp/<Product ID> <Number of Pages of Review on the site>
  ```

  This command will populate the amazonreviewpages.txt with all the necessary values.

3. Now for the command that will bring all this together.
    **Note** If the want the output in output.json then make sure it is empty before running the below command. If not
    then you can run the command with your own output filename.

    ```
    $ scrapy crawl -o output.json amazon_review
    ```

    ```
    $ scrapy crawl -o <your output filename> amazon_review
    ```

**Disclaimer:** Amazon may blacklist your IP address. Jayanth Kanive is not responsible for any damage that may be caused by using this application.
 
**Note** You can vary the download_delay in the ./spider/amazon_review.py to process the request a little slower.
```
download_delay = 10
```
