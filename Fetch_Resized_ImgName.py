import urllib3
from urllib.parse import quote
import requests
import json

def Fetch_Resized_ImgName(url, w_len = 200):
  # Fetch_Resized_ImgName(url) -> len(Fetch_Resized_ImgName(url)):4, 1-> w, 2->h, 3->filename, 4->(w,h)

  quoted_url = "http://18.184.179.85/?img_url=%s&w_len=%d" % (quote(url), w_len)
  #http://haber.ozguruygulama.com/fetch_img_with_rszd   
  r_get_false = False
  
  try:
  
    r = requests.get(quoted_url, allow_redirects=True, timeout=30)
  
  # jsone_encoded = r.content.decode('utf-8')
  
  except:
    
    json_decoded = json.loads("""[{"width":"200","height":"166","filename":"http_haber.ozguruygulama.com_static_h_news.png"}]""") 
    r_get_false = True
  
  if r_get_false == False:
  
    try:
      json_decoded = json.loads(r.text) # jsone_encoded)
    except:
      json_decoded = json.loads("""[{"width":"200","height":"166","filename":"http_haber.ozguruygulama.com_static_h_news.png"}]""")  
  
  res_width = json_decoded[0]["width"]
  res_height = json_decoded[0]["height"]
  res_filename = json_decoded[0]["filename"]
  
  return [res_width, res_height, res_filename, (res_width, res_height)]
