import os
import time

from pytube import YouTube

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        # download the caption by pytube
        start = time.time()
        for yt in data:
            print('downloading caption for', yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue

            if yt.id == 'WPKYpZeFv-0':
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except KeyError:
                print('KeyError for downloading caption for', yt.url)
                continue
            except AttributeError:
                print('AttributeError for downloading caption for', yt.url)
                continue
            # except KeyError, AttributeError:
            #     print('Error for downloading caption for', url)
            #     continue

            # save the file
            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')

        return data


#========================================================
# import time
#
# from youtube_dl import YoutubeDL
#
# from yt_concate.pipeline.steps.step import Step
# from yt_concate.pipeline.steps.step import StepException
#
#
# class DownloadCaptions(Step):
#     def process(self, data, inputs, utils):
#         start = time.time()
#         for yt in data:
#             print('downloading caption for', yt.id)
#             if utils.caption_file_exists(yt):
#                 print('found existing caption file')
#                 continue
#
#             ydl_opt = {
#                 'skip_download': True,
#                 'writesubtitles': True,
#                 'writeautomaticsub': True,
#                 'subtitlelengs': 'en',
#                 'outtmpl': yt.caption_filepath,
#                 'nooverwrites': True,
#             }
#
#             # 取得data中的url給source
#             # print(url)
#             try:
#                 with YoutubeDL(ydl_opt) as ydl:
#                     ydl.download([yt.url])
#
#             except Exception as e:
#                 print(e)
#                 print("An Error occur for", yt.url)
#                 continue
#
#         end = time.time()
#         print('took', end - start, 'seconds')
#
#         return data
#
#
