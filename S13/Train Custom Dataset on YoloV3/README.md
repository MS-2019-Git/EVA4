The output video with 3 classes trained on YoloV3 is at:
https://www.youtube.com/watch?v=ulC3hzPkT7E

Training Custom Dataset on Colab for YoloV3
---------------------------------------------------
Refer to this Colab File: LINK (https://colab.research.google.com/drive/1LbKkQf4hbIuiUHunLlvY-cc0d_sNcAgS)
Refer to this GitHub Repo (https://github.com/theschoolofai/YoloV3)
Collect a dataset of 500 images and annotate them. Please select a class for which you can find a YouTube video as well. Steps are explained in the readme.md file on GitHub.

Once done:
----------
Download (https://www.y2mate.com/en19) a very small (~10-30sec) video from youtube which shows your class. 
Use ffmpeg (https://en.wikibooks.org/wiki/FFMPEG_An_Intermediate_Guide/image_sequence) to extract frames from the video. 
Upload on your drive (alternatively you could be doing all of this on your drive to save upload time)
Inter on these images using detect.py file. **Modify** detect.py file if your file names do not match the ones mentioned on GitHub. 

`python detect.py --conf-thres 0.3 --output output_folder_name`

Use ffmpeg (Links to an external site.) to convert the files in your output folder to video
Upload the video to YouTube. 
Share the link to your GitHub project with the steps as mentioned above
Share the link of your YouTube video
