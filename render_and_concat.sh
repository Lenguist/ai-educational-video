#!/bin/bash

# Render each scene individually
manim -pql dot_product_explanation.py Intro
manim -pql dot_product_explanation.py Definition
manim -pql dot_product_explanation.py Formula
manim -pql dot_product_explanation.py GeometricInterpretation
manim -pql dot_product_explanation.py Conclusion

# Create a list of video files to concatenate
echo "file 'media/videos/dot_product_explanation/480p15/Intro.mp4'" > file_list.txt
echo "file 'media/videos/dot_product_explanation/480p15/Definition.mp4'" >> file_list.txt
echo "file 'media/videos/dot_product_explanation/480p15/Formula.mp4'" >> file_list.txt
echo "file 'media/videos/dot_product_explanation/480p15/GeometricInterpretation.mp4'" >> file_list.txt
echo "file 'media/videos/dot_product_explanation/480p15/Conclusion.mp4'" >> file_list.txt

# Concatenate videos using ffmpeg
ffmpeg -f concat -safe 0 -i file_list_diodes.txt -c copy output-diodes.mp4

# Remove the file list
rm file_list.txt

echo "Rendering and concatenation complete!"
