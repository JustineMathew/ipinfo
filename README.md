# ipinfo
This script will convert IP address into country name.

You need to buld the image using the docker file. The code below can be used for building an image

 >docker build -t image_name .

The below code can used to run the image:
 
 >docker run -it --rm --name pythoninfo -e ACCESS_KEY="accesskey from ipstack" image_name ipaddress
 
 Example: docker run -it --rm --name pythoninfo -e ACCESS_KEY=6d3\58037945226c20d0055228f46579  ipinfo:1 8.8.8.8
 
 The access key can be obtained by folowing the below steps:
 
 - Visit "https://ipstack.com"
 - Click on "Get Free API key"
 - Fill out the details
 - You would get an access key
 
 
