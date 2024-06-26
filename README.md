# Video compression



## H.266

- Compile H.266 from source: https://github.com/fraunhoferhhi/vvenc

- Install requirements to build `ffmpeg`:

  ```bash
  sudo apt install build-essential libtool autoconf automake pkg-config libx11-dev libxext-dev libxrender-dev libxv-dev libjpeg-dev libpng-dev libtiff-dev libwebp-dev libavcodec-dev libavformat-dev libavfilter-dev libavutil-dev libswscale-dev libvorbis-dev libmp3lame-dev libopus-dev libvpx-dev libx264-dev libx265-dev libtheora-dev libopenh264-dev libfaac-dev zlib1g-dev libgsm1-dev:i386
  ```

  Follow instructions to add `libvvenc` to `ffmpeg`: https://github.com/fraunhoferhhi/vvenc/wiki/FFmpeg-Integration

- In `ffmpeg` directory, configure ffmpeg to include `libvvenc`

  ```bash
  ./configure  --enable-pthreads --enable-pic --enable-shared --enable-rpath --arch=amd64 --enable-demuxer=dash --enable-libxml2 --enable-libvvenc --enable-libx264 --enable-gpl
  ```

  Then make and install

  ```bash
  make	#make -j (optional)
  sudo make install
  ```

### Encoding and playing YUV file

- YUV file, 1920x1080 4:2:0 format 16bit depth 120fps

  ```bash
  ffmpeg -f rawvideo -pix_fmt yuv420p -s:v 1920x1080 -r 120 -i input.yuv -c:v libvvenc -q 5 -threads 8 -f rawvideo output.266
  ```

- To play video use `ffmpeg`

  ```bash
  ffplay -strict -2 output.266
  ```

  

