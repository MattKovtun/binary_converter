# Usage
# 1. Install requirements. It's only `PIL (pillow)`
`pip install -r requirements.txt`
# 2. Convert `.txt` with binaries into `.jpg`s.
`python convert.py <filename_with_binaries.txt> <output_directory_for_jpgs>` <br>
For example:
`python convert.py example.txt images_jpg`. This command should take binaries from `example.txt` and output images to `images_jpg` resulting in 1 image.

Pay attention that structure of input file has to match structure which was used previously.<br>
<pre>
ID        FaceImage
1         FFD8FF.......(binary).....
2         89504E47.....(binary).....
.
.
.
</pre>
