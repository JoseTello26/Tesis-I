## Commands



### YUV to Y4M

- Convert YUV files to Y4M container files

  ```bash
  ffmpeg -framerate 25 -video_size 352x288 -pix_fmt yuv420p -i input.yuv input.y4m
  ```



### Get SI-TI 

- Get SI-TI for each video

  ```bash
  siti-tools input.y4m --color-range full > input.json
  ```



### Obtain metrics

- Get PSNR

  ```bash
  fmpeg-quality-metrics output_<codec>_<bitrate>k.264 input.y4m -m psnr --framerate <framerate> -p -v > psnr/<codec>_<bitrate>.txt
  ```

- Get SSIM

  ```bash
  fmpeg-quality-metrics output_<codec>_<bitrate>k.264 input.y4m -m ssim --framerate <framerate> -p -v > psnr/<codec>_<bitrate>.txt
  ```

  

### Compress each video

1. **dog and beauty**

   - H264

     ```bash
     #1024kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 1024k output_h264_1024k.mp4
     ```

     

     ```bash
     #2048kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 2048k output_h264_2048k.mp4
     ```

     

     ```bash
     #4096kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 5096k output_h264_5096k.mp4
     ```

     

   - H265

     

     ```bash
     #1024kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 1024k output_h265_1024k.mp4
     ```

     

     ```bash
     #2048kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 2048k output_h265_2048k.mp4
     ```

     

     ```bash
     #4096kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 5096k output_h265_5096k.mp4
     ```

   - H266

     

     ```bash
     #1024kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libvvenc -q 5 -preset faster -threads 8 -b:v 1024k output_h266_1024k.266
     ```

     

     ```bash
     #2048kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libvvenc -q 5 -preset faster -threads 8 -b:v 2048k output_h266_2048k.266
     ```

     

     ```bash
     #4096kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libvvenc -q 5 -preset faster -threads 8 -b:v 5096k output_h266_5096k.266
     ```

     

   - DVC

2. **news**

   - H264

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 128k output_h264_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 256k output_h264_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 512k output_h264_512k.mp4
     ```

     

   - H265

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 128k output_h265_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 256k output_h265_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 512k output_h265_512k.mp4
     ```

   - H266

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 128k output_h266_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 256k output_h266_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 512k output_h266_512k.mp4
     ```

     

   - DVC

3. **four_people**

   - H264

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 128k output_h264_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 256k output_h264_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 512k output_h264_512k.mp4
     ```

     

   - H265

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 128k output_h265_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 256k output_h265_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 512k output_h265_512k.mp4
     ```

   - H266

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 128k output_h266_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 256k output_h266_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1280x720 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 512k output_h266_512k.mp4
     ```

     

   - DVC

4. **hallroom**

   - H264

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 128k output_h264_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 256k output_h264_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 512k output_h264_512k.mp4
     ```

     

   - H265

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 128k output_h265_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 256k output_h265_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 512k output_h265_512k.mp4
     ```

   - H266

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 128k output_h266_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 256k output_h266_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 25 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 512k output_h266_512k.mp4
     ```

     

   - DVC

5. **ice_skating**

   - H264

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 128k output_h264_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 256k output_h264_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 512k output_h264_512k.mp4
     ```

     

   - H265

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 128k output_h265_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 256k output_h265_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 512k output_h265_512k.mp4
     ```

   - H266

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 128k output_h266_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 256k output_h266_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 512k output_h266_512k.mp4
     ```

     

   - DVC

6. **foreman**

   - H264

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 128k output_h264_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 256k output_h264_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx264 -q 5 -preset faster -threads 8 -b:v 512k output_h264_512k.mp4
     ```

     

   - H265

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 128k output_h265_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 256k output_h265_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libx265 -q 5 -preset faster -threads 8 -b:v 512k output_h265_512k.mp4
     ```

   - H266

     

     ```bash
     #128kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 128k output_h266_128k.mp4
     ```

     

     ```bash
     #256kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 256k output_h266_256k.mp4
     ```

     

     ```bash
     #512kbps
     ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 352x288 -r 30 -i input.yuv -c:v libvvenc -q 5 -preset fast -threads 8 -b:v 512k output_h266_512k.mp4
     ```

     

   - DVC



