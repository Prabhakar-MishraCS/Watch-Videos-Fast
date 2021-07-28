
from selenium import webdriver

import traceback
import time
from selenium.webdriver.firefox.options import Options
import webbrowser

options = Options()
#options.headless = True
driver = webdriver.Firefox(options=options)
hyperlink = "https://www.youtube.com/c/FlyingBeast320/videos" #Channel URL of your favourite youtuber
print("\nProcess Started\n")

while True:
    try:
        driver.get(hyperlink)

        time.sleep(5)
        # xpath of first vide
        x = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]')
        #x.click()
        z=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/ytd-thumbnail/a')
        #print(x.text)


        def favYoutubersVid(fb, t=1, a=3):

            time = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/div[1]/div[1]/div/div[1]/div[2]/span[2]')
            time_ago = time.text
            #print(time_ago)

            #time_ago = x.li.find_next_sibling('li').text
            sec_ago = convert_to_seconds(time_ago)
            #print(sec_ago)
            if sec_ago < 1 * 60 * 60: #Checking every hour
                # author = vidSoup.title.text[2:-11]
                video_title = x.text
                #print(video_title)
                vid_url = z.get_attribute('href')
                print(video_title + '\n' + time_ago + '\n' + vid_url)
                webbrowser.open(vid_url)


        def convert_to_seconds(time):
            t = int(time[0:2])
            if 'minutes' in time:
                return t * 60
            elif 'hour' in time:
                return t * 60 * 60
            elif 'day' in time:
                return t * 24 * 60 * 60
            elif 'week' in time:
                return t * 7 * 24 * 60 * 60


        fb = 'https://www.youtube.com/c/FlyingBeast320/videos'

        video_haru = favYoutubersVid(fb, 3)
        time.sleep(60)


    except:
        print(traceback.format_exc())
    finally:
        driver.quit()
